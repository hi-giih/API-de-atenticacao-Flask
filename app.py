from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager,login_user, current_user,logout_user, login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = "you-secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
    dado= request.json
    username = dado.get("username")
    password = dado.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password: 
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação feita com sucesso"})
    
    return jsonify({"message": "As credenciais estão inválidas"}), 400


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

@app.route("/user", methods=["POST"])
def create_user():
    dado = request.json
    username = dado.get("username")
    password = dado.get("password")    

    if username and password:
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify ({"message":"Usuario Cadstrado com sucesso"})
    
    return jsonify({"message":"Dados invalidos"}), 400

@app.route("/user/<int:id_user>", methods=["GET"])
def read_user(id_user):
    user = User.query.get(id_user)
    if user:
        return {"userame": user.username}
    
    return jsonify({"message":"Usuario não encontrado"}), 404

@app.route("/user/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):
    dado = request.json
    user = User.query.get(id_user)

    if user and dado.get("password"):
        user.password = dado.get("password")
        db.session.commit()
        return jsonify({"message":f"Usuario {id_user} ataulizado com sucesso"})
    
    return jsonify({"message":"Usuario não encontrado"}), 404


@app.route("/user/<int:id_user>", methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if id_user == current_user:
        return jsonify({"message":"Deleção não permitida"}),403

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message":"Usuario deletado com sucesso"})
    return jsonify({"message":"Usuario não encontrado"}),404


if __name__ == '__main__':
    app.run(debug=True)
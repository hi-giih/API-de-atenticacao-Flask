# 👥 API de Autenticação de Usuários com Flask

## 📄 Descrição

Este projeto é uma API de autenticação de usuários desenvolvida com o microframework Flask em Python. A aplicação permite o cadastro, login, logout, e atualização de dados dos usuários, com conexão ao banco de dados MySQL local. Este projeto foi criado com fins educacionais para praticar conceitos de APIs REST, autenticação e integração com banco de dados relacional.


## ⚙️ Funcionalidades

- ✅ **Cadastro de Usuário:** Criação de novos usuários com dados como nome, e-mail e senha.
- 🔐 **Login de Usuário:** Autenticação via e-mail e senha, com retorno de token de sessão ou status.
- 🚪 **Logout de Usuário:** Finalização de sessão do usuário.
- ✏️ **Atualização de Usuário:** Permite alterar as informações do perfil do usuário autenticado.
- ❌ **Deletar Usuário:** Permite deletar um usuário
- 📬 **Integração com Banco de Dados MySQL:** Todos os dados são persistidos em um banco de dados relacional local.



## 💻 Tecnologias Utilizadas

- **Python 3.11**
- **Flask 2.3.0**
- **Flask-Login**
- **Flask-SQLAlchemy**
- **MySQL** (via `pymysql` connector)



## 🚀 Instalando e Rodando o Projeto

1. Clone este repositório:
```
git clone git@github.com:seu-usuario/API-Autenticacao-Flask.git
```

2. Acesse o diretório do projeto:
```
cd API-Autenticacao-Flask
```

3. Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
```

4. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

5. Instale as dependências:
```
pip install -r requeriments.txt
```

6. Configure a string de conexão com o banco MySQL:
```
app.config['SQLALCHEMY_DATABASE_URI'] = 
```

7. Execute a aplicação:
```
python app.py
```

O servidor estará disponível em: `http://127.0.0.1:5000`




## 🔧 Futuras Melhorias
Implementação de autenticação via JWT.
Melhoria nas validações de entrada.
Criação de testes automatizados com pytest.
Paginação e filtros para listagem de usuários.
Deploy em nuvem com Docker + Heroku ou Render


## 📜 Licença
Este projeto não está sob nenhuma licença específica.

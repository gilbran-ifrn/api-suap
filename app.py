import os

from flask import Flask, redirect, request, session, url_for

from flask_login import UserMixin
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

# Configurações OAuth2 do SUAP
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = "https://suap.ifrn.edu.br/o/authorize/"
TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
REDIRECT_URI = os.getenv("REDIRECT_URI")
API_BASE_URL = "https://suap.ifrn.edu.br/api/"

# Carregar variáveis do .env
load_dotenv()

# Permite utilizar o OAuth sem HTTPS
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Para gerenciar a sessão

class User(UserMixin):
    def __init__(self, id, nome, email, token):
        self.id = id
        self.nome = nome
        self.email = email
        self.token = token  # Token OAuth do SUAP

login_manager = LoginManager()
login_manager.login_view = "login"  # Rota de login
login_manager.init_app(app)

# Usuários ativos armazenados em memória (exemplo)
users = {}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Página inicial
@app.route("/")
def index():
    return '<a href="/login">Entrar com SUAP</a>'

# Rota de login
@app.route("/login")
def login():
    suap = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = suap.authorization_url(AUTH_URL)

    session['oauth_state'] = state
    return redirect(authorization_url)

# Callback do SUAP (deve ser configurado no cadastro da aplicação)
@app.route("/callback")
def callback():
    suap = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, state=session.get("oauth_state"))

    token = suap.fetch_token(
        TOKEN_URL,
        authorization_response=request.url,
        client_secret=CLIENT_SECRET
    )

    suap = OAuth2Session(CLIENT_ID, token=token)
    perfil = suap.get(API_BASE_URL + "/rh/eu/").json()

    user = User(
        id=str(perfil["identificacao"]),
        nome=perfil["nome_usual"],
        email=perfil["email"],
        token=token
    )
    users[user.id] = user
    login_user(user)

    return redirect(url_for("perfil"))

# Rota protegida: exibe informações do usuário logado
@app.route("/perfil")
@login_required
def perfil():
    suap = OAuth2Session(CLIENT_ID, token=current_user.token)
    dados = suap.get(API_BASE_URL + "/rh/eu/").json()

    return f"<h1>Olá, {dados['nome_usual']}</h1>"

#logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("logout_sucesso"))

@app.route("/logout-sucesso")
def logout_sucesso():
    return """
    <h1>Você saiu com sucesso.</h1>
    <p>Obrigado por utilizar a aplicação!</p>
    <a href='/'>Voltar à página inicial</a> | <a href='/login'>Entrar novamente</a>
    """
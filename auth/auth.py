from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from requests_oauthlib import OAuth2Session

from models import Usuario

from extensions import loggin_manager
from extensions import CLIENT_ID
from extensions import CLIENT_SECRET
from extensions import AUTH_URL
from extensions import TOKEN_URL
from extensions import REDIRECT_URI
from extensions import API_BASE_URL

from dotenv import load_dotenv

auth_bp = Blueprint (
    'auth_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth/static/'
)

# Carregar variáveis do .env
load_dotenv()

# Usuários ativos armazenados em memória (exemplo)
users = {}

@loggin_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@loggin_manager.unauthorized_handler
def naoAutorizado():
    return render_template('auth/index.html', notLogin=True)


# Rota de login
@auth_bp.route("/login")
def login():
    suap = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = suap.authorization_url(AUTH_URL)

    session['oauth_state'] = state
    return redirect(authorization_url)

# Callback do SUAP (deve ser configurado no cadastro da aplicação)
@auth_bp.route("/callback")
def callback():
    suap = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, state=session.get("oauth_state"))

    token = suap.fetch_token(
        TOKEN_URL,
        authorization_response=request.url,
        client_secret=CLIENT_SECRET
    )

    suap = OAuth2Session(CLIENT_ID, token=token)
    perfil = suap.get(API_BASE_URL + "/rh/eu/").json()

    user = Usuario(
        id=str(perfil["identificacao"]),
        nome=perfil["nome_usual"],
        email=perfil["email"],
        token=token
    )
    users[user.id] = user
    login_user(user)

    return redirect(url_for("auth_bp.dash"))


#logout
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.logout_sucesso"))

@auth_bp.route("/logout-sucesso")
def logout_sucesso():
    return """
    <h1>Você saiu com sucesso.</h1>
    <p>Obrigado por utilizar a aplicação!</p>
    <a href='/'>Voltar à página inicial</a> | <a href='/login'>Entrar novamente</a>
    """

# Página inicial
@auth_bp.route("/")
def index():
    return render_template('auth/index.html')

# Rota protegida: exibe informações do usuário logado
@auth_bp.route("/dash")
@login_required
def dash():
    suap = OAuth2Session(CLIENT_ID, token=current_user.token)
    dados = suap.get(API_BASE_URL + "/rh/eu/").json()

    return render_template('auth/dash.html')
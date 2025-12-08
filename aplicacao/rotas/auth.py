from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    session,
    url_for
)

from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user
)

from requests_oauthlib import OAuth2Session

from aplicacao.utils.models import Usuario

from aplicacao.utils.extensions import (
    loggin_manager, 
    CLIENT_ID,
    CLIENT_SECRET,
    AUTH_URL,
    TOKEN_URL,
    REDIRECT_URI,
    API_BASE_URL
)

import logging
import sys
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

auth_bp = Blueprint (
    'auth_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/'
)

# Usuários ativos armazenados em memória (exemplo)
users = {}

@loggin_manager.user_loader
def load_user(user_id):
    logging.info(f"Load_User: {users}")
    try:
        return users.get(user_id) 
    except (ValueError, KeyError):
        return None

@loggin_manager.unauthorized_handler
def naoAutorizado():
    return render_template('auth/index.html')


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
    try:
        suap = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, state=session.get("oauth_state"))

        token = suap.fetch_token(
            TOKEN_URL,
            authorization_response=request.url,
            client_secret=CLIENT_SECRET
        )
    except Exception as e:
        return f'Erro: {str(e)}<br><a href="/">Voltar</a>'

    try:
        suap = OAuth2Session(CLIENT_ID, token=token)
        perfil = suap.get(API_BASE_URL + "/api/rh/eu/").json()

        user = Usuario(
            matricula=str(perfil["identificacao"]),
            nome=perfil["nome_usual"],
            email=perfil["email"],
            token=token
        )
        # Adiciona o usuário ao armazenamento em memória
        users[user.id] = user

        # Verificação de valor atribuído corretamente
        if user.id in users and users.get(user.id) is not None:
            logging.info(f"Usuário {user.nome} adicionado com sucesso.")
        else:
            logging.error(f"Falha ao adicionar o usuário {user.nome}.")

        login_user(user)

        return redirect(url_for("auth_bp.dash"))
    except Exception as e:
        return f'Erro: {str(e)}<br><a href="/">Voltar</a>'

#logout
@auth_bp.route("/logout")
@login_required
def logout():
    # remove o usuário do armazenamento em memória e descarta o valor retornado
    _ = users.pop(current_user.id, None)

    # Verificação de valor atribuído corretamente
    if current_user.id in users:
        logging.info(f"Usuário {current_user.id} não foi removido.")
    else:
        logging.error(f"Usuário {current_user.id} foi removido com sucesso.")


    logout_user()
    return redirect(url_for("auth_bp.index"))
    #return redirect("https://suap.ifrn.edu.br/o/logout/?next=" + url_for("index", _external=True))


# Página inicial
@auth_bp.route("/")
def index():
    return render_template('auth/index.html')


# Rota protegida: exibe informações do usuário logado
@auth_bp.route("/dash")
@login_required
def dash():
    return render_template('dash.html')

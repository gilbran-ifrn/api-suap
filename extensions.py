import os

from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import LoginManager

from models import Usuario

from requests_oauthlib import OAuth2Session

loggin_manager = LoginManager()

# Configurações OAuth2 do SUAP
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = "https://suap.ifrn.edu.br/o/authorize/"
TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
REDIRECT_URI = os.getenv("REDIRECT_URI")
API_BASE_URL = "https://suap.ifrn.edu.br/api/"

def feedback(endpoint, secao):
    suap = OAuth2Session(CLIENT_ID, token=current_user.token)
    resposta = suap.get(API_BASE_URL + endpoint)

    print(f"= = = = = = = = = = =")
    print(f"CÓDIGO: {resposta.status_code}")
    print(f"= = = = = = = = = = =")

    if resposta.status_code == 200:
        dados = resposta.json()
        return render_template('exibeDados.html', dados=dados, secao=secao)
    elif resposta.status_code == 401:
        dados = resposta.json()
        return render_template('exibeErro.html', erro='401', mens=dados['detail'], secao=secao)
    else:
        return render_template('exibeErro.html', erro=resposta.status_code, mens=dados['detail'], secao=secao)
import os

from flask import Flask

from extensions import loggin_manager

from auth.auth import auth_bp
from comum.comum import comum_bp
from ponto.ponto import ponto_bp
from rh.rh import rh_bp

# Permite utilizar o OAuth sem HTTPS
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Para gerenciar a sessão

loggin_manager.login_view = "login"  # Rota de login
loggin_manager.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(comum_bp, url_prefix='/comum')
app.register_blueprint(ponto_bp, url_prefix='/ponto')
app.register_blueprint(rh_bp, url_prefix='/rh')




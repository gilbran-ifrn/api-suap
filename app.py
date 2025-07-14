import os

from flask import Flask

from extensions import loggin_manager

from auth.auth import auth_bp
from comum.comum import comum_bp
from contracheques.contracheques import contracheques_bp
from demandas.demandas import demandas_bp
from edu.edu import edu_bp
from eventos.eventos import eventos_bp
from ferias.ferias import ferias_bp
from pesquisa.pesquisa import pesquisa_bp
from ponto.ponto import ponto_bp
from portaria.portaria import portaria_bp
from protocolo.protocolo import protocolo_bp
from catalogo_provedor_servico.catalogo_provedor_servico import catalogo_provedor_servico_bp
from rh.rh import rh_bp
from api_deprecated.api_deprecated import api_deprecated_bp

# Permite utilizar o OAuth sem HTTPS
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Para gerenciar a sessão

loggin_manager.login_view = "login"  # Rota de login
loggin_manager.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(comum_bp, url_prefix='/comum')
app.register_blueprint(contracheques_bp, url_prefix='/contracheques')
app.register_blueprint(demandas_bp, url_prefix='/demandas')
app.register_blueprint(edu_bp, url_prefix='/edu')
app.register_blueprint(eventos_bp, url_prefix='/eventos')
app.register_blueprint(ferias_bp, url_prefix='/ferias')
app.register_blueprint(pesquisa_bp, url_prefix='/pesquisa')
app.register_blueprint(ponto_bp, url_prefix='/ponto')
app.register_blueprint(portaria_bp, url_prefix='/portaria')
app.register_blueprint(protocolo_bp, url_prefix='/protocolo')
app.register_blueprint(catalogo_provedor_servico_bp, url_prefix='/provedor-servicos')
app.register_blueprint(rh_bp, url_prefix='/rh')
app.register_blueprint(api_deprecated_bp, url_prefix='/api-deprecated')





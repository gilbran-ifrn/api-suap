from flask import Blueprint
from flask import render_template
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

rh_bp = Blueprint (
    'rh_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/rh/static/'
)

# Página inicial
@rh_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="rh")

@rh_bp.route("/eu")
@login_required
def eu():
    return feedback("/rh/eu/", "rh")

@rh_bp.route("/unidades-organizacionais")
@login_required
def unidadesOrganizacionais():
    return feedback("/rh/unidades-organizacionais/", "rh")

@rh_bp.route("/servidores")
@login_required
def servidores():
    return feedback("/rh/servidores/", "rh")

@rh_bp.route("/servidores-detalhado")
@login_required
def servidorDetalhado():
    return feedback("/rh/servidores/detalhado/", "rh")

@rh_bp.route("/servidores-integra")
@login_required
def servidorIntegra():
    return feedback("/rh/servidores/integra/", "rh")

@rh_bp.route("/setores")
@login_required
def setores():
    return feedback("/rh/setores/", "rh")

@rh_bp.route("/historico-funcional")
@login_required
def historicoFuncional():
    return feedback("/rh/meu-historico-funcional/", "rh")

@rh_bp.route("/meus-afastamentos")
@login_required
def afastamentos():
    return feedback("/rh/minhas-ocorrencias-afastamentos/", "rh")

@rh_bp.route("/carteira-funcional")
@login_required
def carteiraFuncional():
    matricula = '3567818'
    return feedback(f"/rh/emitir-carteira-funcional-digital/{matricula}/", "rh")
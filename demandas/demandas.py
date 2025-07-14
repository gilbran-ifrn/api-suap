from flask import Blueprint
from flask import render_template
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

demandas_bp = Blueprint (
    'demandas_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/demandas/static/'
)

# Página inicial
@demandas_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="demandas")

@demandas_bp.route("/atualizacoes")
@login_required
def atualizacoes():
    return feedback("/api/demandas/atualizacoes/", "demandas")
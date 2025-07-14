from flask import Blueprint
from flask import render_template
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

eventos_bp = Blueprint (
    'eventos_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/eventos/static/'
)

# Página inicial
@eventos_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="eventos")

@eventos_bp.route("/banners-ativos")
@login_required
def atualizacoes():
    return feedback("/api/eventos/banners/ativos/", "eventos")
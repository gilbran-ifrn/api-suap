from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from app.utils.models import Usuario
from app.utils.extensions import API_BASE_URL
from app.utils.extensions import loggin_manager
from app.utils.extensions import feedback

# Carregar variáveis do .env

comunicacaoSocial_bp = Blueprint (
    'comunicacaoSocial_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/comunicacao/static/'
)

@comunicacaoSocial_bp.route("/banners")
@login_required
def banners():
    return feedback("/api/midia/banners/", "eventos")

@comunicacaoSocial_bp.route("/ativos-deferidos")
@login_required
def bannersAtivo():
    return feedback("/api/midia/eventos/ativos-deferidos/", "eventos")
from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from aplicacao.utils.models import Usuario
from aplicacao.utils.extensions import API_BASE_URL
from aplicacao.utils.extensions import loggin_manager
from aplicacao.utils.extensions import obterRecurso

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
    return obterRecurso("/api/midia/banners/")

@comunicacaoSocial_bp.route("/ativos-deferidos")
@login_required
def bannersAtivo():
    return obterRecurso("/api/midia/eventos/ativos-deferidos/")
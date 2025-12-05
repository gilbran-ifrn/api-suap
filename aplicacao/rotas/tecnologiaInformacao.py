from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from aplicacao.utils.models import Usuario
from aplicacao.utils.extensions import API_BASE_URL
from aplicacao.utils.extensions import loggin_manager
from aplicacao.utils.extensions import feedback

tecnologiaInformacao_bp = Blueprint (
    'tecnologiaInformacao_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/tecnologiaInformacao/static/'
)


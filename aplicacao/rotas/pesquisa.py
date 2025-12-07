from flask import Blueprint
from flask import render_template
from flask_login import login_required
from aplicacao.utils.extensions import obterRecurso


pesquisa_bp = Blueprint (
    'pesquisa_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/'
)

@pesquisa_bp.route("/projetos")
@login_required
def projetos():
    return obterRecurso("/api/pesquisa/projetos/")
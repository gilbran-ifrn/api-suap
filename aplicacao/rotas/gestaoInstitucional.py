from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from aplicacao.utils.models import Usuario
from aplicacao.utils.extensions import API_BASE_URL
from aplicacao.utils.extensions import loggin_manager
from aplicacao.utils.extensions import obterRecurso


gestaoInstitucional_bp = Blueprint (
    'gestaoInstitucional_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/gestaoInstitucional/static/'
)

@gestaoInstitucional_bp.route("/estatisticas")
@login_required
def suapNumeros():
    return obterRecurso("/api/institucional/estatisticas/")

@gestaoInstitucional_bp.route("/consulta-documentos", methods=["GET","POST"])
@login_required
def consultaPublica():
    if request.method == 'POST':
        i = request.form.get('identificador')
        a = request.form.get('assunto')

        if i == '':
            i = None
        if a == '':
            a = None

        params = {
            'identificador': i,
            'assunto': a
        }

        return obterRecurso("/api/institucional/consulta_publica/documentos/", params)
    else:
        a = 'gestaoInstitucional_bp.consultaPublica'
        f = [
	            { "rotulo":"Identificador", "tipo":"text", "id":"identificador", "obrigatorio":"" },
                { "rotulo":"Assunto", "tipo":"text", "id":"assunto", "obrigatorio":"" },
        ]
        return render_template('exibeForm.html', action=a, form=f)
from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from aplicacao.utils.models import Usuario
from aplicacao.utils.extensions import API_BASE_URL
from aplicacao.utils.extensions import loggin_manager
from aplicacao.utils.extensions import obterRecurso

administracao_bp = Blueprint (
    'administracao_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/administracao/static/'
)

@administracao_bp.route("/meus-processos", methods=["GET","POST"])
@login_required
def meusProcessos():
    if request.method == 'POST':
        a = request.form.get('assunto')
        s = request.form.get('status')
        uo = request.form.get('uo')
        dc = request.form.get('data_cadastro')

        if a == '':
            a = None
        if s == '':
            s = None
        if uo == '':
            uo = None
        if dc == '':
            dc = None

        params = {
            'assunto': a,
            'status': s,
            'uo': uo,
            'data_cadastro': dc
        }

        return obterRecurso("/api/administracao/meus-processos-fisicos/", "protocolo", params)
    else:
        a = 'administracao_bp.meusProcessos'
        f = [
	            { "rotulo":"Assunto", "tipo":"text", "id":"assunto", "obrigatorio":"" },
                { "rotulo":"Status", "tipo":"number", "id":"status", "obrigatorio":"" },
                { "rotulo":"UO", "tipo":"text", "id":"uo", "obrigatorio":"" },
                { "rotulo":"Data Cadastro", "tipo":"date", "id":"data_cadastro", "obrigatorio":"" }
            ]
        return render_template('exibeForm.html', action=a, form=f, secao='protocolo')


@administracao_bp.route("/processo-especifico", methods=["GET","POST"])
@login_required
def processoEspecifico():
    if request.method == 'POST':
        pk = request.form.get('pk')

        params = {
            'pk': pk
        }

        print(params)

        return obterRecurso(f"/api/administracao/meu-processo-fisico/{params['pk']}/")
    else:
        a = 'administracao_bp.processoEspecifico'
        f = [
	            { "rotulo":"PK", "tipo":"number", "id":"pk", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f)
    
@administracao_bp.route("/validar-visitante", methods=["GET","POST"])
@login_required
def validarVisitante():
    if request.method == 'POST':
        cw = request.form.get('chave_wifi')

        params = {
            'chave_wifi': cw
        }

        print (params)

        return obterRecurso(f"/api/administracao/validar-visitante-portaria/{params['chave_wifi']}/")
    else:
        a = 'administracao_bp.validarVisitante'
        f = [
	            { "rotulo":"Chave WiFi", "tipo":"text", "id":"chave_wifi", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f)

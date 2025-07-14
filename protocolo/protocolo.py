from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

protocolo_bp = Blueprint (
    'protocolo_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/protocolo/static/'
)

# Página inicial
@protocolo_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="protocolo")

@protocolo_bp.route("/meus-processos", methods=["GET","POST"])
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

        return feedback("/api/protocolo/meus-processos/", "protocolo", params)
    else:
        a = 'protocolo_bp.meusProcessos'
        f = [
	            { "rotulo":"Assunto", "tipo":"text", "id":"assunto", "obrigatorio":"" },
                { "rotulo":"Status", "tipo":"number", "id":"status", "obrigatorio":"" },
                { "rotulo":"UO", "tipo":"text", "id":"uo", "obrigatorio":"" },
                { "rotulo":"Data Cadastro", "tipo":"date", "id":"data_cadastro", "obrigatorio":"" }
            ]
        return render_template('exibeForm.html', action=a, form=f, secao='protocolo')


@protocolo_bp.route("/processo-especifico", methods=["GET","POST"])
@login_required
def processoEspecifico():
    if request.method == 'POST':
        pk = request.form.get('pk')

        params = {
            'pk': pk
        }

        print(params)

        return feedback(f"/api/protocolo/meu-processo/{params['pk']}/", "protocolo")
    else:
        a = 'protocolo_bp.processoEspecifico'
        f = [
	            { "rotulo":"PK", "tipo":"number", "id":"pk", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='protocolo')
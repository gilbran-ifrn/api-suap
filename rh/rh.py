from flask import Blueprint
from flask import render_template
from flask import request
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
    return feedback("/api/rh/eu/", "rh")

@rh_bp.route("/unidades-organizacionais")
@login_required
def unidadesOrganizacionais():
    return feedback("/api/rh/unidades-organizacionais/", "rh")

@rh_bp.route("/servidores", methods=["GET","POST"])
@login_required
def servidores():
    if request.method == 'POST':
        n = request.form.get('nome')
        c = request.form.get('campus')
        m = request.form.get('matricula')
        s = request.form.get('setor')
        ce = request.form.get('cargo_emprego')

        if n == '':
            n = None
        if c == '':
            c = None
        if m == '':
            m = None
        if s == '':
            s = None
        if ce == '':
            ce = None

        params = {
            'nome': n,
            'campus': c,
            'matricula': m,
            'setor': s,
            'cargo_emprego': ce
        }

        return feedback("/api/rh/servidores/", "rh", params)
    else:
        a = 'rh_bp.servidores'
        f = [
	            { "rotulo":"Nome", "tipo":"text", "id":"nome", "obrigatorio":"" },
                { "rotulo":"Campus", "tipo":"text", "id":"campus", "obrigatorio":"" },
                { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"" },
                { "rotulo":"Setor", "tipo":"text", "id":"setor", "obrigatorio":"" },
                { "rotulo":"Cargo Emprego", "tipo":"text", "id":"cargo_emprego", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

@rh_bp.route("/servidores-detalhado", methods=["GET","POST"])
@login_required
def servidorDetalhado():
    if request.method == 'POST':
        n = request.form.get('nome')
        c = request.form.get('campus')
        m = request.form.get('matricula')
        s = request.form.get('setor')
        ce = request.form.get('cargo_emprego')

        if n == '':
            n = None
        if c == '':
            c = None
        if m == '':
            m = None
        if s == '':
            s = None
        if ce == '':
            ce = None

        params = {
            'nome': n,
            'campus': c,
            'matricula': m,
            'setor': s,
            'cargo_emprego': ce
        }

        return feedback("/api/rh/servidores/detalhado/", "rh", params)
    else:
        a = 'rh_bp.servidorDetalhado'
        f = [
	            { "rotulo":"Nome", "tipo":"text", "id":"nome", "obrigatorio":"" },
                { "rotulo":"Campus", "tipo":"text", "id":"campus", "obrigatorio":"" },
                { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"" },
                { "rotulo":"Setor", "tipo":"text", "id":"setor", "obrigatorio":"" },
                { "rotulo":"Cargo Emprego", "tipo":"text", "id":"cargo_emprego", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

@rh_bp.route("/servidores-integra")
@login_required
def servidorIntegra():
    return feedback("/api/rh/servidores/integra/", "rh")

@rh_bp.route("/setores", methods=["GET","POST"])
@login_required
def setores():
    if request.method == 'POST':
        n = request.form.get('nome')
        s = request.form.get('sigla')
        u = request.form.get('uo')
        e = request.form.get('excluido')
        av = request.form.get('areas_vinculacao')

        if n == '':
            n = None
        if s == '':
            s = None
        if u == '':
            u = None
        if e == '':
            e = None
        else:
            e.lower() == 'true' # garantir que é boolean
        if av == '':
            av = None

        params = {
            'nome': n,
            'sigla': s,
            'uo': u,
            'excluido': e,
            'areas_vinculacao': av
        }

        print (params)

        return feedback("/api/rh/setores/", "rh", params)
    else:
        a = 'rh_bp.setores'
        f = [
	            { "rotulo":"Nome", "tipo":"text", "id":"nome", "obrigatorio":"" },
                { "rotulo":"Sigla", "tipo":"text", "id":"sigla", "obrigatorio":"" },
                { "rotulo":"UO (em 13.7.25 este campo estava com problema)", "tipo":"text", "id":"uo", "obrigatorio":"" },
                { "rotulo":"Excluído (True|False)", "tipo":"text", "id":"excluido", "obrigatorio":"" },
                { "rotulo":"Área Vinculação", "tipo":"text", "id":"areas_vinculacao", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

@rh_bp.route("/historico-funcional")
@login_required
def historicoFuncional():
    return feedback("/api/rh/meu-historico-funcional/", "rh")

@rh_bp.route("/meus-afastamentos")
@login_required
def afastamentos():
    return feedback("/api/rh/minhas-ocorrencias-afastamentos/", "rh")

@rh_bp.route("/carteira-funcional", methods=["GET","POST"])
@login_required
def carteiraFuncional():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        print (params)

        return feedback(f"/api/rh/emitir-carteira-funcional-digital/{params['matricula']}/", "rh")
    else:
        a = 'rh_bp.carteiraFuncional'
        f = [
	            { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

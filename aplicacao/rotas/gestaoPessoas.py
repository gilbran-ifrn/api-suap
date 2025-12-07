from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from aplicacao.utils.models import Usuario
from aplicacao.utils.extensions import API_BASE_URL
from aplicacao.utils.extensions import loggin_manager
from aplicacao.utils.extensions import obterRecurso


gestaoPessoas_bp = Blueprint (
    'gestaoPessoas_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/gestaoPessoas/static/'
)

@gestaoPessoas_bp.route("/meus-dados")
@login_required
def meusDados():
    return obterRecurso("/api/rh/meus-dados/"  )

@gestaoPessoas_bp.route("/eu")
@login_required
def eu():
    return obterRecurso("/api/rh/eu/"  )

@gestaoPessoas_bp.route("/unidades-organizacionais")
@login_required
def unidadesOrganizacionais():
    return obterRecurso("/api/rh/unidades-organizacionais/"  )

@gestaoPessoas_bp.route("/servidores", methods=["GET","POST"])
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

        return obterRecurso("/api/rh/servidores/"  , params)
    else:
        a = 'gestaoPessoas_bp.servidores'
        f = [
	            { "rotulo":"Nome", "tipo":"text", "id":"nome", "obrigatorio":"" },
                { "rotulo":"Campus", "tipo":"text", "id":"campus", "obrigatorio":"" },
                { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"" },
                { "rotulo":"Setor", "tipo":"text", "id":"setor", "obrigatorio":"" },
                { "rotulo":"Cargo Emprego", "tipo":"text", "id":"cargo_emprego", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')
    
@gestaoPessoas_bp.route("/servidores-detalhado", methods=["GET","POST"])
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

        return obterRecurso("/api/rh/servidores/detalhado/"  , params)
    else:
        a = 'gestaoPessoas_bp.servidorDetalhado'
        f = [
	            { "rotulo":"Nome", "tipo":"text", "id":"nome", "obrigatorio":"" },
                { "rotulo":"Campus", "tipo":"text", "id":"campus", "obrigatorio":"" },
                { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"" },
                { "rotulo":"Setor", "tipo":"text", "id":"setor", "obrigatorio":"" },
                { "rotulo":"Cargo Emprego", "tipo":"text", "id":"cargo_emprego", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')
    

@gestaoPessoas_bp.route("/servidores-integra")
@login_required
def servidorIntegra():
    return obterRecurso("/api/rh/servidores/integra/"  )

@gestaoPessoas_bp.route("/setores", methods=["GET","POST"])
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

        return obterRecurso("/api/rh/setores/"  , params)
    else:
        a = 'gestaoPessoas_bp.setores'
        f = [
	            { "rotulo":"Nome", "tipo":"text", "id":"nome", "obrigatorio":"" },
                { "rotulo":"Sigla", "tipo":"text", "id":"sigla", "obrigatorio":"" },
                { "rotulo":"UO (em 13.7.25 este campo estava com problema)", "tipo":"text", "id":"uo", "obrigatorio":"" },
                { "rotulo":"Excluído (True|False)", "tipo":"text", "id":"excluido", "obrigatorio":"" },
                { "rotulo":"Área Vinculação", "tipo":"text", "id":"areas_vinculacao", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

@gestaoPessoas_bp.route("/historico-funcional")
@login_required
def historicoFuncional():
    return obterRecurso("/api/rh/meu-historico-funcional/"  )

@gestaoPessoas_bp.route("/meus-afastamentos")
@login_required
def afastamentos():
    return obterRecurso("/api/rh/minhas-ocorrencias-afastamentos/"  )

@gestaoPessoas_bp.route("/carteira-funcional", methods=["GET","POST"])
@login_required
def carteiraFuncional():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        print (params)

        return obterRecurso(f"/api/rh/emitir-carteira-funcional-digital/{params['matricula']}/"  )
    else:
        a = 'gestaoPessoas_bp.carteiraFuncional'
        f = [
	            { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

@gestaoPessoas_bp.route("/minhas-ferias")
@login_required
def minhasFerias():
    return obterRecurso("/api/rh/minhas-ferias/", "ferias")

@gestaoPessoas_bp.route("/minhas-frequencias")
@login_required
def minhaFrequencia():
    return obterRecurso("/api/rh/minhas-frequencias/", "ponto")

@gestaoPessoas_bp.route("/servidor-resumido", methods=["GET","POST"])
@login_required
def servidorResumido():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        print (params)

        return obterRecurso(f"/api/rh/servidor-resumido/"  , params)
    else:
        a = 'gestaoPessoas_bp.servidorResumido'
        f = [
	            { "rotulo":"Matrícula", "tipo":"text", "id":"matricula" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')

@gestaoPessoas_bp.route("/meus-contracheques")
@login_required
def meusContracheques():
    return obterRecurso("/api/rh/meus-contracheques/", "contracheques")

@gestaoPessoas_bp.route("/meu-contracheque", methods=["GET","POST"])
@login_required
def meuContracheque():
    if request.method == 'POST':
        an = request.form.get('ano')
        m = request.form.get('mes')

        params = {
            'ano': an,
            'mes': m
        }

        print (params)

        return obterRecurso(f"/api/rh/meu-contracheque/{params['ano']}/{params['mes']}/", "contracheques")
    else:
        a = 'gestaoPessoas_bp.meuContracheque'
        f = [
	            { "rotulo":"Ano", "tipo":"number", "id":"ano", "obrigatorio":"required" },
                { "rotulo":"Mês", "tipo":"number", "id":"mes", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='contracheques')

@gestaoPessoas_bp.route("/contracheques")
@login_required
def contracheques():
    return obterRecurso("/api/rh/contracheques/", "contracheques")
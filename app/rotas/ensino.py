from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from app.utils.models import Usuario
from app.utils.extensions import API_BASE_URL
from app.utils.extensions import loggin_manager
from app.utils.extensions import feedback

ensino_bp = Blueprint (
    'ensino_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/ensino/static/'
)


@ensino_bp.route("/periodos")
@login_required
def periodos():
    return feedback("/api/ensino/periodos/", 'edu')


@ensino_bp.route("/diario-semestre", methods=["GET","POST"])
@login_required
def diarioSemestre():
    if request.method == 'POST':
        s = request.form.get('semestre')

        params = {
            'semestre': s
        }

        return feedback(f"/api/ensino/diarios/{params['semestre']}", 'edu')
    else:
        a = 'ensino_bp.diarioSemestre'
        f = [
	            { "rotulo":"Semestre", "tipo":"text", "id":"semestre", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/diario-professores", methods=["GET","POST"])
@login_required
def diarioProfessores():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/ensino/diarios/{params['id_diario']}/professores", 'edu')
    else:
        a = 'ensino_bp.diarioProfessores'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/diario-alunos", methods=["GET","POST"])
@login_required
def diarioAlunos():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/ensino/diarios/{params['id_diario']}/alunos", 'edu')
    else:
        a = 'ensino_bp.diarioAlunos'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/diario-aulas", methods=["GET","POST"])
@login_required
def diarioAulas():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/ensino/diarios/{params['id_diario']}/aulas", 'edu')
    else:
        a = 'ensino_bp.diarioAulas'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/diario-materiais", methods=["GET","POST"])
@login_required
def diarioMateriais():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/ensino/diarios/{params['id_diario']}/materiais", 'edu')
    else:
        a = 'ensino_bp.diarioMateriais'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/material", methods=["GET","POST"])
@login_required
def material():
    if request.method == 'POST':
        idM = request.form.get('id_material')

        params = {
            'id_material': idM
        }

        return feedback(f"/api/ensino/materiais/{params['id_material']}", 'edu')
    else:
        a = 'ensino_bp.material'
        f = [
	            { "rotulo":"ID Material", "tipo":"number", "id":"id_material", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/material-pdf", methods=["GET","POST"])
@login_required
def materialPDF():
    if request.method == 'POST':
        idD = request.form.get('id_diario')
        idM = request.form.get('id_material')

        params = {
            'id_diario': idD,
            'id_material': idM
        }

        return feedback(f"/api/ensino/materiais/{params['id_diario']}/{params['id_material']}/pdf/", 'edu')
    else:
        a = 'ensino_bp.materialPDF'
        f = [
                { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" },
	            { "rotulo":"ID Material", "tipo":"number", "id":"id_material", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/trabalhos", methods=["GET","POST"])
@login_required
def trabalhos():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/ensino/diarios/{params['id_diario']}/trabalhos", 'edu')
    else:
        a = 'ensino_bp.trabalhos'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/topicos", methods=["GET","POST"])
@login_required
def topicos():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/ensino/diarios/{params['id_diario']}/topicos", 'edu')
    else:
        a = 'ensino_bp.topicos'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/disciplinas", methods=["GET","POST"])
@login_required
def disciplinas():
    if request.method == 'POST':
        s = request.form.get('semestre')

        params = {
            'semestre': s
        }

        return feedback(f"/api/ensino/disciplinas/{params['semestre']}", 'edu')
    else:
        a = 'ensino_bp.disciplinas'
        f = [
	            { "rotulo":"Semestre", "tipo":"text", "id":"semestre", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/disciplina-etapa", methods=["GET","POST"])
@login_required
def disciplinaEtapa():
    if request.method == 'POST':
        d = request.form.get('disciplina')

        params = {
            'disciplina': d
        }

        return feedback(f"/api/ensino/disciplinas/{params['disciplina']}/etapas/", 'edu')
    else:
        a = 'ensino_bp.disciplinaEtapa'
        f = [
	            { "rotulo":"Semestre", "tipo":"number", "id":"disciplina", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/mensagens", methods=["GET","POST"])
@login_required
def mensagens():
    if request.method == 'POST':
        s = request.form.get('status')

        params = {
            'status': s
        }

        return feedback(f"/api/ensino/mensagens/entrada/{params['status']}", 'edu')
    else:
        a = 'ensino_bp.mensagens'
        f = [
	            { "rotulo":"Status (nao_lisdas, lidas, todas, lixeira)", "tipo":"text", "id":"status", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/dados-aluno")
@login_required
def dadosAluno():
    return feedback("/api/ensino/meus-dados-aluno/", 'edu')

@ensino_bp.route("/requisito-conclusao")
@login_required
def requisitoConclusao():
    return feedback("/api/ensino/requisitos-conclusao/", 'edu')

@ensino_bp.route("/aluno-boletim", methods=["GET","POST"])
@login_required
def alunoBoletim():
    if request.method == 'POST':
        al = request.form.get('ano_letivo')
        pl = request.form.get('periodo_letivo')

        params = {
            'ano_letivo': al,
            'periodo_letivo': pl
        }

        return feedback(f"/api/ensino/meu-boletim/{params['ano_letivo']}/{params['periodo_letivo']}/", 'edu')
    else:
        a = 'ensino_bp.alunoBoletim'
        f = [
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"required" },
	            { "rotulo":"Período Letivo", "tipo":"number", "id":"periodo_letivo", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')

@ensino_bp.route("/aluno-diarios", methods=["GET","POST"])
@login_required
def alunoDiarios():
    if request.method == 'POST':
        al = request.form.get('ano_letivo')
        pl = request.form.get('periodo_letivo')

        params = {
            'ano_letivo': al,
            'periodo_letivo': pl
        }

        return feedback(f"/api/ensino/meus-diarios/{params['ano_letivo']}/{params['periodo_letivo']}/", 'edu')
    else:
        a = 'ensino_bp.alunoDiarios'
        f = [
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"required" },
	            { "rotulo":"Período Letivo", "tipo":"number", "id":"periodo_letivo", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')

@ensino_bp.route("/aluno-periodo-letivo")
@login_required
def alunoPeriodoLetivo():
    return feedback("/api/ensino/meus-periodos-letivos/", 'edu')

@ensino_bp.route("/aluno-avaliacoes")
@login_required
def alunoAvaliacoes():
    return feedback("/api/ensino/minhas-proximas-avaliacoes/", 'edu')

@ensino_bp.route("/aluno-turma-virtual", methods=["GET","POST"])
@login_required
def alunoTurmaVirtual():
    if request.method == 'POST':
        pk = request.form.get('pk')

        params = {
            'pk': pk
        }

        return feedback(f"/api/ensino/minha-turma-virtual/{params['pk']}/", 'edu')
    else:
        a = 'ensino_bp.alunoTurmaVirtual'
        f = [
	            { "rotulo":"PK", "tipo":"number", "id":"pk", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')

@ensino_bp.route("/aluno-turma-virtual-especifico", methods=["GET","POST"])
@login_required
def alunoTurmaVirtualEspecifico():
    if request.method == 'POST':
        al = request.form.get('ano_letivo')
        pl = request.form.get('periodo_letivo')

        params = {
            'ano_letivo': al,
            'periodo_letivo': pl
        }

        return feedback(f"/api/ensino/minhas-turmas-virtuais/{params['ano_letivo']}/{params['periodo_letivo']}/", 'edu')
    else:
        a = 'ensino_bp.alunoTurmaVirtualEspecifico'
        f = [
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"required" },
	            { "rotulo":"Período Letivo", "tipo":"number", "id":"periodo_letivo", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    

@ensino_bp.route("/meu-diario-ead", methods=["GET","POST"])
@login_required
def meuDiarioEad():
    if request.method == 'POST':
        pk = request.form.get('pk')

        params = {
            'pk': pk
        }

        return feedback(f"/api/ensino/meus-diarios-ead/{params['pk']}/", 'edu')
    else:
        a = 'ensino_bp.meuDiarioEad'
        f = [
	            { "rotulo":"PK", "tipo":"number", "id":"pk", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')

@ensino_bp.route("/meus-diarios-ead")
@login_required
def meusDiariosEad():
    return feedback("/api/ensino/meus-diarios-ead/", 'edu')


@ensino_bp.route("/dados-aluno-matriculado", methods=["GET","POST"])
@login_required
def dadosAlunoMatriculado():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        return feedback(f"/api/ensino/aluno-matriculado/", 'edu', params)
    else:
        a = 'ensino_bp.dadosAlunoMatriculado'
        f = [
	            { "rotulo":"Matricula", "tipo":"text", "id":"matricula", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='edu')
    
@ensino_bp.route("/portal-professores")
@login_required
def portalProfessores():
    return feedback("/api/ensino/portal-professores/", 'edu')
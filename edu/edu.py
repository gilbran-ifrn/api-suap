from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

secaoAtual = 'edu'

edu_bp = Blueprint (
    'edu_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/edu/static/'
)

# Página inicial
@edu_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao=secaoAtual)

@edu_bp.route("/periodos")
@login_required
def periodos():
    return feedback("/api/edu/periodos", secaoAtual)


@edu_bp.route("/diario-semestre", methods=["GET","POST"])
@login_required
def diarioSemestre():
    if request.method == 'POST':
        s = request.form.get('semestre')

        params = {
            'semestre': s
        }

        return feedback(f"/api/edu/diarios/{params['semestre']}", secaoAtual)
    else:
        a = 'edu_bp.diarioSemestre'
        f = [
	            { "rotulo":"Semestre", "tipo":"text", "id":"semestre", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/diario-professores", methods=["GET","POST"])
@login_required
def diarioProfessores():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/edu/diarios/{params['id_diario']}/professores", secaoAtual)
    else:
        a = 'edu_bp.diarioProfessores'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/diario-alunos", methods=["GET","POST"])
@login_required
def diarioAlunos():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/edu/diarios/{params['id_diario']}/alunos", secaoAtual)
    else:
        a = 'edu_bp.diarioAlunos'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/diario-aulas", methods=["GET","POST"])
@login_required
def diarioAulas():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/edu/diarios/{params['id_diario']}/aulas", secaoAtual)
    else:
        a = 'edu_bp.diarioAulas'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/diario-materiais", methods=["GET","POST"])
@login_required
def diarioMateriais():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/edu/diarios/{params['id_diario']}/materiais", secaoAtual)
    else:
        a = 'edu_bp.diarioMateriais'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/material", methods=["GET","POST"])
@login_required
def material():
    if request.method == 'POST':
        idM = request.form.get('id_material')

        params = {
            'id_material': idM
        }

        return feedback(f"/api/edu/materiais/{params['id_material']}", secaoAtual)
    else:
        a = 'edu_bp.material'
        f = [
	            { "rotulo":"ID Material", "tipo":"number", "id":"id_material", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/material-pdf", methods=["GET","POST"])
@login_required
def materialPDF():
    if request.method == 'POST':
        idD = request.form.get('id_diario')
        idM = request.form.get('id_material')

        params = {
            'id_diario': idD,
            'id_material': idM
        }

        return feedback(f"/api/edu/materiais/{params['id_diario']}/{params['id_material']}/pdf/", secaoAtual)
    else:
        a = 'edu_bp.materialPDF'
        f = [
                { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" },
	            { "rotulo":"ID Material", "tipo":"number", "id":"id_material", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/trabalhos", methods=["GET","POST"])
@login_required
def trabalhos():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/edu/diarios/{params['id_diario']}/trabalhos", secaoAtual)
    else:
        a = 'edu_bp.trabalhos'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/topicos", methods=["GET","POST"])
@login_required
def topicos():
    if request.method == 'POST':
        idD = request.form.get('id_diario')

        params = {
            'id_diario': idD
        }

        return feedback(f"/api/edu/diarios/{params['id_diario']}/topicos", secaoAtual)
    else:
        a = 'edu_bp.topicos'
        f = [
	            { "rotulo":"ID Diário", "tipo":"number", "id":"id_diario", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/disciplinas", methods=["GET","POST"])
@login_required
def disciplinas():
    if request.method == 'POST':
        s = request.form.get('semestre')

        params = {
            'semestre': s
        }

        return feedback(f"/api/edu/disciplinas/{params['semestre']}", secaoAtual)
    else:
        a = 'edu_bp.disciplinas'
        f = [
	            { "rotulo":"Semestre", "tipo":"text", "id":"semestre", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/disciplina-etapa", methods=["GET","POST"])
@login_required
def disciplinaEtapa():
    if request.method == 'POST':
        d = request.form.get('disciplina')

        params = {
            'disciplina': d
        }

        return feedback(f"/api/edu/disciplinas/{params['disciplina']}/etapas/", secaoAtual)
    else:
        a = 'edu_bp.disciplinaEtapa'
        f = [
	            { "rotulo":"Semestre", "tipo":"number", "id":"disciplina", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/mensagens", methods=["GET","POST"])
@login_required
def mensagens():
    if request.method == 'POST':
        s = request.form.get('status')

        params = {
            'status': s
        }

        return feedback(f"/api/edu/mensagens/entrada/{params['status']}", secaoAtual)
    else:
        a = 'edu_bp.mensagens'
        f = [
	            { "rotulo":"Status (nao_lisdas, lidas, todas, lixeira)", "tipo":"text", "id":"status", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
@edu_bp.route("/dados-aluno")
@login_required
def dadosAluno():
    return feedback("/api/edu/meus-dados-aluno/", secaoAtual)

@edu_bp.route("/requisito-conclusao")
@login_required
def requisitoConclusao():
    return feedback("/api/edu/requisitos-conclusao/", secaoAtual)

@edu_bp.route("/aluno-boletim", methods=["GET","POST"])
@login_required
def alunoBoletim():
    if request.method == 'POST':
        al = request.form.get('ano_letivo')
        pl = request.form.get('periodo_letivo')

        params = {
            'ano_letivo': al,
            'periodo_letivo': pl
        }

        return feedback(f"/api/edu/meu-boletim/{params['ano_letivo']}/{params['periodo_letivo']}/", secaoAtual)
    else:
        a = 'edu_bp.alunoBoletim'
        f = [
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"required" },
	            { "rotulo":"Período Letivo", "tipo":"number", "id":"periodo_letivo", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/aluno-diarios", methods=["GET","POST"])
@login_required
def alunoDiarios():
    if request.method == 'POST':
        al = request.form.get('ano_letivo')
        pl = request.form.get('periodo_letivo')

        params = {
            'ano_letivo': al,
            'periodo_letivo': pl
        }

        return feedback(f"/api/edu/meus-diarios/{params['ano_letivo']}/{params['periodo_letivo']}/", secaoAtual)
    else:
        a = 'edu_bp.alunoDiarios'
        f = [
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"required" },
	            { "rotulo":"Período Letivo", "tipo":"number", "id":"periodo_letivo", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/aluno-periodo-letivo")
@login_required
def alunoPeriodoLetivo():
    return feedback("/api/edu/meus-periodos-letivos/", secaoAtual)

@edu_bp.route("/aluno-avaliacoes")
@login_required
def alunoAvaliacoes():
    return feedback("/api/edu/minhas-proximas-avaliacoes/", secaoAtual)

@edu_bp.route("/aluno-turma-virtual", methods=["GET","POST"])
@login_required
def alunoTurmaVirtual():
    if request.method == 'POST':
        pk = request.form.get('pk')

        params = {
            'pk': pk
        }

        return feedback(f"/api/edu/minha-turma-virtual/{params['pk']}/", secaoAtual)
    else:
        a = 'edu_bp.alunoTurmaVirtual'
        f = [
	            { "rotulo":"PK", "tipo":"number", "id":"pk", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/aluno-turma-virtual-especifico", methods=["GET","POST"])
@login_required
def alunoTurmaVirtualEspecifico():
    if request.method == 'POST':
        al = request.form.get('ano_letivo')
        pl = request.form.get('periodo_letivo')

        params = {
            'ano_letivo': al,
            'periodo_letivo': pl
        }

        return feedback(f"/api/edu/minhas-turmas-virtuais/{params['ano_letivo']}/{params['periodo_letivo']}/", secaoAtual)
    else:
        a = 'edu_bp.alunoTurmaVirtualEspecifico'
        f = [
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"required" },
	            { "rotulo":"Período Letivo", "tipo":"number", "id":"periodo_letivo", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/dados-aluno-siabe", methods=["GET","POST"])
@login_required
def dadosAlunoSiabe():
    if request.method == 'POST':
        m = request.form.get('matricula')
        ac = request.form.get('ano_conclusao')
        cc = request.form.get('codigo_curso')

        if m == '':
            m = None
        if ac == '':
            ac = None
        if cc == '':
            cc = None

        params = {
            'matricula': m,
            'ano_conclusao': ac,
            'codigo_curso': cc
        }

        return feedback("/api/edu/dados-aluno-siabi/", secaoAtual, params)
    else:
        a = 'rh_bp.dadosAlunoSiabe'
        f = [
	            { "rotulo":"Matricula", "tipo":"text", "id":"matricula", "obrigatorio":"" },
                { "rotulo":"Ano Conclusão", "tipo":"text", "id":"ano_conclusao", "obrigatorio":"" },
                { "rotulo":"Código Curso", "tipo":"text", "id":"codigo_curso", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/meu-diario-ead", methods=["GET","POST"])
@login_required
def meuDiarioEad():
    if request.method == 'POST':
        pk = request.form.get('pk')

        params = {
            'pk': pk
        }

        return feedback(f"/api/edu/meus-diarios-ead/{params['pk']}/", secaoAtual)
    else:
        a = 'edu_bp.meuDiarioEad'
        f = [
	            { "rotulo":"PK", "tipo":"number", "id":"pk", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/meus-diarios-ead")
@login_required
def meusDiariosEad():
    return feedback("/api/edu/meus-diarios-ead/", secaoAtual)


@edu_bp.route("/dados-aluno-matriculado", methods=["GET","POST"])
@login_required
def dadosAlunoMatriculado():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        return feedback(f"/api/ensino/aluno-matriculado/", secaoAtual, params)
    else:
        a = 'edu_bp.dadosAlunoMatriculado'
        f = [
	            { "rotulo":"Matricula", "tipo":"text", "id":"matricula", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

###################################################################
######################   DEPRECATED   #############################
###################################################################

@edu_bp.route("/dados-servidor", methods=["GET","POST"])
@login_required
def dadosServidor():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        return feedback(f"/api/edu/dados_servidor/", secaoAtual, params)
    else:
        a = 'edu_bp.dadosServidor'
        f = [
	            { "rotulo":"Matricula", "tipo":"text", "id":"matricula", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/listar-alunos-atualizados", methods=["GET","POST"])
@login_required
def listarAlunosAtualizados():
    if request.method == 'POST':
        d = request.form.get('data')

        params = {
            'data': d
        }

        return feedback(f"/api/edu/listar_alunos_atualizados/", secaoAtual, params)
    else:
        a = 'edu_bp.listarAlunosAtualizados'
        f = [
	            { "rotulo":"Data", "tipo":"text", "id":"data", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/listar-cursos", methods=["GET","POST"])
@login_required
def listarCursos():
    if request.method == 'POST':
        sc = request.form.get('sigla_campus')
        pl = request.form.get('periodo_letivo')
        al = request.form.get('ano_letivo')
        c = request.form.get('codigo')

        if sc == '':
            sc = None
        if pl == '':
            pl = None
        if al == '':
            al = None
        if c == '':
            c = None

        params = {
            'sigla_campus': sc,
            'periodo_letivo': pl,
            'ano_letivo': al,
            'codigo': c
        }

        return feedback("/api/edu/listar_cursos/", secaoAtual, params)
    else:
        a = 'rh_bp.listarCursos'
        f = [
	            { "rotulo":"Sigla Campus", "tipo":"text", "id":"sigla_campus", "obrigatorio":"" },
                { "rotulo":"Período Letivo", "tipo":"text", "id":"periodo_letivo", "obrigatorio":"" },
                { "rotulo":"Ano Letivo", "tipo":"number", "id":"ano_letivo", "obrigatorio":"" },
                { "rotulo":"Código", "tipo":"text", "id":"codigo", "obrigatorio":"" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/listar-matrizes", methods=["GET","POST"])
@login_required
def listarMatrizes():
    if request.method == 'POST':
        sc = request.form.get('sigla_campus')

        params = {
            'sigla_campus': sc
        }

        return feedback(f"/api/edu/listar_matrizes/", secaoAtual, params)
    else:
        a = 'edu_bp.listarMatrizes'
        f = [
	            { "rotulo":"Sigla Campus", "tipo":"text", "id":"sigla_campus", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)

@edu_bp.route("/listar-vinculos-matrizes")
@login_required
def listarVinculosMatrizes():
    return feedback("/api/edu/listar_vinculos_matrizes_cursos/", secaoAtual)

@edu_bp.route("/listar-cursos-ead", methods=["GET","POST"])
@login_required
def listarCursosEad():
    return feedback("/api/edu/listar_cursos_ead/", secaoAtual)

@edu_bp.route("/listar-turmas-ead", methods=["GET","POST"])
@login_required
def listarTurmasEad():
    return feedback("/api/edu/listar_turmas_ead/", secaoAtual)

@edu_bp.route("/listar-diarios-ead", methods=["GET","POST"])
@login_required
def listarDiariosEad():
    return feedback("/api/edu/listar_diarios_ead/", secaoAtual)

@edu_bp.route("/listar-professores-ead", methods=["GET","POST"])
@login_required
def listarProfessoresEad():
    return feedback("/api/edu/listar_professores_ead/", secaoAtual)

@edu_bp.route("/listar-alunos-ead", methods=["GET","POST"])
@login_required
def listarAlunosEad():
    return feedback("/api/edu/listar_alunos_ead/", secaoAtual)

@edu_bp.route("/listar-polos-ead", methods=["GET","POST"])
@login_required
def listarPolosEad():
    return feedback("/api/edu/listar_polos_ead/", secaoAtual)

@edu_bp.route("/listar-campus-ead", methods=["GET","POST"])
@login_required
def listarCamposEad():
    return feedback("/api/edu/listar_campus_ead/", secaoAtual)

@edu_bp.route("/listar-componentes-ead", methods=["GET","POST"])
@login_required
def listarComponentesEad():
    return feedback("/api/edu/listar_componentes_curriculares_ead/", secaoAtual)

@edu_bp.route("/listar-diarios-aluno", methods=["GET","POST"])
@login_required
def listarDiariosAluno():
    if request.method == 'POST':
        m = request.form.get('matricula')

        params = {
            'matricula': m
        }

        return feedback(f"/api/edu/listar_diarios_aluno/{params['matricula']}/", secaoAtual)
    else:
        a = 'edu_bp.listarDiariosAluno'
        f = [
	            { "rotulo":"Matrícula", "tipo":"text", "id":"matricula", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao=secaoAtual)
    
from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

contracheques_bp = Blueprint (
    'contracheques_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/contracheques/static/'
)

# Página inicial
@contracheques_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="contracheques")

@contracheques_bp.route("/meus-contracheques")
@login_required
def meusContracheques():
    return feedback("/api/contracheques/meus-contracheques/", "contracheques")


@contracheques_bp.route("/meu-contracheque", methods=["GET","POST"])
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

        return feedback(f"/api/contracheques/meu-contracheque/{params['ano']}/{params['mes']}/", "contracheques")
    else:
        a = 'contracheques_bp.meuContracheque'
        f = [
	            { "rotulo":"Ano", "tipo":"number", "id":"ano", "obrigatorio":"required" },
                { "rotulo":"Mês", "tipo":"number", "id":"mes", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='rh')


@contracheques_bp.route("/contracheques")
@login_required
def contracheques():
    return feedback("/api/contracheques/contracheques/", "contracheques")
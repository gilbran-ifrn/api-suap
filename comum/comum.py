from flask import Blueprint
from flask import render_template
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

comum_bp = Blueprint (
    'comum_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/comum/static/'
)

# Página inicial
@comum_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="comum")

@comum_bp.route("/meus-dados")
@login_required
def meusDados():
    return feedback("comum/meus-dados/", "comum")

@comum_bp.route("/suap-em-numeros")
@login_required
def suapNumeros():
    return feedback("comum/suap-em-numeros/", "comum")
    
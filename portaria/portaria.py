from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required
from models import Usuario
from extensions import feedback
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

portaria_bp = Blueprint (
    'portaria_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/portaria/static/'
)

# Página inicial
@portaria_bp.route("/")
@login_required
def index():
    return render_template('exibeInicio.html', secao="portaria")

@portaria_bp.route("/validar-visitante", methods=["GET","POST"])
@login_required
def validarVisitante():
    if request.method == 'POST':
        cw = request.form.get('chave_wifi')

        params = {
            'chave_wifi': cw
        }

        print (params)

        return feedback(f"/api/portaria/validar-visitante/{params['chave_wifi']}/", "portaria")
    else:
        a = 'portaria_bp.validarVisitante'
        f = [
	            { "rotulo":"Chave WiFi", "tipo":"text", "id":"chave_wifi", "obrigatorio":"required" }
        ]
        return render_template('exibeForm.html', action=a, form=f, secao='portaria')
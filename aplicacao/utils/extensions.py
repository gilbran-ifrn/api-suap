import os

from flask import (
    render_template
)

from flask_login import (
    login_user,
    logout_user,
    current_user,
    LoginManager
)

from requests_oauthlib import OAuth2Session

loggin_manager = LoginManager()

# Variáveis para OAuth2 do SUAP
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
AUTH_URL = "https://suap.ifrn.edu.br/o/authorize/"
TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
API_BASE_URL = "https://suap.ifrn.edu.br"
LOGOUT_URL = "https://suap.ifrn.edu.br/comum/logout"

def obterRecurso(endpoint, params=None):
    try:
        suap = OAuth2Session(CLIENT_ID, token=current_user.token)

        if params:
            resposta = suap.get(API_BASE_URL + endpoint, params=params)
        else:
            resposta = suap.get(API_BASE_URL + endpoint)

        #if not resposta.ok:
        #    return f"Erro {resposta.status_code}. Deu merda"

        print (resposta.headers)

        print(f"= = = = = = = = = = =")
        print(f"CÓDIGO: {resposta.status_code}")
        print(f"= = = = = = = = = = =")

        if resposta.status_code == 200:
            dados = resposta.json()
            return render_template('exibeDados.html', dados=dados )
        elif resposta.status_code == 500:
            dados = {'mens':'A bronca é do lado do SUAP, não do frontend!'}
            return render_template('exibeErro.html', erro=resposta.status_code, mens=dados )
        else:
            dados = resposta.json()
            #if resposta:
            #    dados = resposta.json()
            #else:
            #    dados = {'mens':'Não acho que a bronca é minha!'}
            return render_template('exibeErro.html', erro=resposta.status_code, mens=dados )
    except Exception as e:
        return f'Erro: {str(e)}<br><a href="/">Voltar</a>'
    

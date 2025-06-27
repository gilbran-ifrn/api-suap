import os

from flask_login import LoginManager

loggin_manager = LoginManager()

# Configurações OAuth2 do SUAP
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = "https://suap.ifrn.edu.br/o/authorize/"
TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
REDIRECT_URI = os.getenv("REDIRECT_URI")
API_BASE_URL = "https://suap.ifrn.edu.br/api/"
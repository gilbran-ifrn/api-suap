import requests
import json

# Detalhes do cliente
client_id = "x5h47Q1ViartNq4kWSnO7i21ZDQI4OPKhvOG3rd7"
client_secret = "uSU1Sp33lduaqXclOhZDnBjJ7LyqLPNCELfvm0MDLnDtmjEJXMTWcGIV8jIsfIWFhLtof0QURpv26NOt2GGkqYaeUDAOHAC1A9qAdcLhmMOSayPwm2gEFZvPpcjua2PT"

# URL do provedor de autenticação
token_url = "https://suap.ifrn.edu.br/o/authorize/"

def obter_token():
    # Parâmetros necessários para obter o token de acesso
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    # Solicita o token de acesso
    response = requests.post(token_url, data=data)

    if response.status_code == 200:
        token_data = json.loads(response.text)
        return token_data["access_token"]
    else:
        print("Erro ao obter o token de acesso.")
        print(response.status_code)
        print(response.content)
        return None

def obter_nome_usuario(token):
    # URL do endpoint para obter o nome do usuário
    user_info_url = "/api/v2/minhas-informacoes/meus-dados/"

    # Configura o cabeçalho de autenticação
    headers = {
        "Authorization": "Bearer " + token
    }

    # Faz a solicitação para obter o nome do usuário
    response = requests.get(user_info_url, headers=headers)

    if response.status_code == 200:
        user_data = json.loads(response.text)
        nome_usuario = user_data["name"]
        print("Nome do usuário:", nome_usuario)
    else:
        print("Erro ao obter o nome do usuário.")

# Obtém o token de acesso
access_token = obter_token()

if access_token:
    # Obtém o nome do usuário usando o token de acesso
    obter_nome_usuario(access_token)

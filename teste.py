import requests

# URL de autorização
authorization_url = 'https://suap.ifrn.edu.br/oauth2/authorize/'

# URL para obter o token de acesso
token_url = 'https://suap.ifrn.edu.br/oauth2/token/'

# Informações do cliente (fornecidas pelo provedor de serviço)
client_id = '3567818'
client_secret = '!pixota1708'

# Redirecionar URL (definida durante o registro do aplicativo)
redirect_uri = 'https://gilbran-ifrn.github.io/aweb'

# Escopo (permissões) solicitado pelo aplicativo
scope = 'dados_academicos dados_funcionais'

# Passo 1: Obter o código de autorização
def obter_codigo_autorizacao():
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': scope
    }
    response = requests.get(authorization_url, params=params)
    response.raise_for_status()
    return response.url

# Passo 2: Trocar o código de autorização pelo token de acesso
def obter_token_acesso(codigo_autorizacao):
    data = {
        'grant_type': 'authorization_code',
        'code': codigo_autorizacao,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    response = requests.post(token_url, data=data)
    response.raise_for_status()
    return response.json()

# Executando o fluxo de autenticação
url_autorizacao = obter_codigo_autorizacao()
# Aqui você precisa abrir a URL `codigo_autorizacao` no navegador e obter o código de autorização após o usuário fornecer consentimento
print('Por favor, acesse a seguinte URL para autorizar o aplicativo:')
print(url_autorizacao)

# Passo 3: Obter o código de autorização do usuário
codigo_autorizacao = input('Digite o código de autorização: ')

token_acesso = obter_token_acesso(codigo_autorizacao)
access_token = token_acesso['access_token']
refresh_token = token_acesso['refresh_token']

# A partir daqui, você pode usar o access_token para fazer chamadas autenticadas à API SUAP

# Exemplo de chamada autenticada
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
response = requests.get('https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/', headers=headers)
response.raise_for_status()
data = response.json()

# Você pode armazenar o access_token e o refresh_token para uso futuro e renovar o token quando necessário

# Renovar o token de acesso
def renovar_token(refresh_token):
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(token_url, data=data)
    response.raise_for_status()
    return response.json()

novo_token_acesso = renovar_token(refresh_token)
novo_access_token = novo_token_acesso['access_token']


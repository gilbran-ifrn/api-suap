import requests

# Defina a URL da API
url = "https://suap.ifrn.edu.br/api/campi/"

# Defina os parâmetros (se houver)
params = {
    "parametro1": "valor1",
    "parametro2": "valor2"
}

# Defina os cabeçalhos (se necessário)
headers = {
    "Authorization": "Token de Autenticação",
    "Content-Type": "application/json"
}

# Faça a chamada GET à API
response = requests.get(url, params=params, headers=headers)

# Verifique o código de status da resposta
if response.status_code == 200:
    # A solicitação foi bem-sucedida
    data = response.json()
    # Faça algo com os dados retornados
    print(data)
else:
    # A solicitação não foi bem-sucedida
    print("Erro na solicitação:", response.status_code)
    print("Mensagem de erro:", response.text)

import requests

url = "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzkxMDg3MywiaWF0IjoxNjg3ODI0NDczLCJqdGkiOiIwNDg0MDVlZTFkZTc0M2FlYWJmNTI3MzNmYTlhZGU0NSIsInVzZXJfaWQiOjU2MzAxfQ.cxuNJwtvZbnuxxgQA5FyXozlyvZaFH_ZWLYfjFV7CUg"

headers = {
    "Authorization": f"JWT {token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Faça algo com os dados retornados
    print("Dados do usuário:", data)
else:
    print("Erro na solicitação:", response.status_code)
    print("Mensagem de erro:", response.text)

import requests
import hashlib

url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"
username = "3567818"
password = "!pixota1708"

# Convertendo a senha para o formato de hash MD5
#password_md5 = hashlib.md5(password.encode()).hexdigest()

payload = {
    "username": username,
    "password": password
}

response = requests.post(url, data=payload)

if response.status_code == 200:
   token_data = response.json()
   for i in token_data:
       print (i)
#    print(token_data)
#    access_token = token_data["access"]
    # Faça algo com o access_token
#    print("Token de acesso obtido:", access_token)


#    url = "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
#    token = access_token

#    headers = {
#        "Authorization": f"JWT {token}",
#        "Content-Type": "application/json"
#    }

#    response = requests.get(url, headers=headers)

#    if response.status_code == 200:
#        data = response.json()
        # Faça algo com os dados retornados
#        print("Dados do usuário:", data)
#    else:
#        print("Erro na solicitação:", response.status_code)
#        print("Mensagem de erro:", response.text)

else:
    print("Erro na solicitação de token:", response.status_code)
    print("Mensagem de erro:", response.text)
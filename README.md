# Projeto Flask - Autenticação SUAP via OAuth2

Este projeto é uma aplicação Flask que permite autenticação de usuários via OAuth2 utilizando a API do SUAP do IFRN. Após o login, o usuário pode visualizar seus dados protegidos na API.

---

## 🚀 Pré-requisitos

- Python 3.8 ou superior
- Git (opcional)
- Ambiente virtual Python (recomendado)

---

## ⚙️ Configuração do Ambiente Local

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
REDIRECT_URI=http://localhost:5000/callback
```

> ⚠️ **Importante:**\
> O arquivo `.env` **não deve ser enviado para o GitHub.** Certifique-se de que ele está listado no arquivo `.gitignore`.

---

## 🛠️ Executando o Projeto

Inicie o servidor Flask:

```bash
python app.py
```

Acesse o sistema no navegador:

```text
http://localhost:5000
```

---

## 🔄 Fluxo de Autenticação

1. O usuário clica em "Entrar com SUAP".
2. O sistema redireciona para o SUAP para autenticação.
3. Após o login, o SUAP retorna um código de autorização.
4. O sistema troca o código pelo token OAuth2.
5. O usuário pode acessar as rotas protegidas.

---

## ✅ Recursos Implementados

- Autenticação OAuth2 via SUAP
- Gerenciamento de sessões com Flask-Login
- Logout seguro com tela de confirmação
- Consulta de dados protegidos da API do SUAP

---

## 📂 Estrutura Recomendada

```
suap-flask-auth/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## 🔒 Segurança

- O arquivo `.env` está no `.gitignore` e **não deve ser versionado.**
- Nunca exponha `CLIENT_SECRET` ou `CLIENT_ID` diretamente no código.
- Em produção, utilize HTTPS para garantir a segurança das credenciais.


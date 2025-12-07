from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, matricula, nome, email, token):
        self.id = matricula
        self.nome = nome
        self.email = email
        self.token = token  # Token OAuth do SUAP
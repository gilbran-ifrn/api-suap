from flask import Flask

from app.utils.extensions import loggin_manager

import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)  # Para gerenciar a sessão

    loggin_manager.login_view = "login"  # Rota de login
    loggin_manager.init_app(app)

    # Registrando blueprints
    from app.rotas.auth import auth_bp
    from app.rotas.administracao import administracao_bp
    from app.rotas.comunicacaoSocial import comunicacaoSocial_bp
    from app.rotas.ensino import ensino_bp
    from app.rotas.gestaoInstitucional import gestaoInstitucional_bp
    from app.rotas.gestaoPessoas import gestaoPessoas_bp
    from app.rotas.pesquisa import pesquisa_bp
    from app.rotas.tecnologiaInformacao import tecnologiaInformacao_bp

    

    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(administracao_bp, url_prefix='/administracao')
    app.register_blueprint(comunicacaoSocial_bp, url_prefix='/comunicacao-social')
    app.register_blueprint(ensino_bp, url_prefix='/ensino')
    app.register_blueprint(gestaoInstitucional_bp, url_prefix='/gestao-institucional')
    app.register_blueprint(gestaoPessoas_bp, url_prefix='/gestao-pessoas')
    app.register_blueprint(pesquisa_bp, url_prefix='/pesquisa')
    app.register_blueprint(tecnologiaInformacao_bp, url_prefix='/tecnologia-informacao')

    return app
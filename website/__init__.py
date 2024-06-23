from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def application():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'for example'

    #app.config['SQLALCHEMY_DATABASE_URI'] = f':///{}'

    from .view import view
    from .auth_file import auth

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app

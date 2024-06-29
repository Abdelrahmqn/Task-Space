from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from my_app.auth import auth
db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)
NAME = "datab.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{NAME}'

app.register_blueprint(auth, url_prefix='/auth')
from my_app import routes

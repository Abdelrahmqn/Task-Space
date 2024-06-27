#!/usr/bin/python3
""" """
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import UserMixin
from sqlalchemy.sql import func


db = SQLAlchemy()
NAME = "datab.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{NAME}'
db.init_app(app)


def create_database():
    """ """
    if not path.exists('website/' + NAME):
        with app.app_context():
            db.create_all()
            print("created")


class User(db.Model, UserMixin):
    first_name = db.Column(db.String(200))
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    notes = db.relationship('Notes')


class Notes(db.Model):
    text = db.Column(db.String(20000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class ToDoList():
    """ """
    pass

@app.route('/')
@app.route('/Home')
@app.route('/home')
def home_page():
    """ """
    return render_template("home.html")


@app.route('/login')
def log_in():
    """ """
    return render_template("login.html")


@app.route('/sign-up')
def sign_up():
    """ """
    return render_template("website/templates/login.html")


@app.route('/logout')
def logout():
    """ """
    return render_template("logout.html")


if __name__ == "__main__":
    create_database()
    app.run(debug=True)

#!/usr/bin/python3
""" """
from flask import Flask, render_template, url_for, flash, redirect, request
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


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    """ """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('passwrod')
        user = User.query.filter_by(email=email)
        if user:
            flash('logged in!', category='success')
        else:
            flash('login error, try again.', category='error')
    else:
        flash('Email error, try again.', category='error')
    return render_template("login.html", boolean=True)


@app.route('/sign-up')
def sign_up():
    """ """
    email = request.form.get('gmail')
    first_name = request.form.get('first_name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    if len(email) < 5:
        flash('email must be greater than 5 characters', category='error')
    elif len(first_name) < 2:
        flash('your first name must be greater than 2 characters', category='error')
    elif password != password2:
        flash('Your passwords don\'t match', category='error')
    elif len(password) < 8:
        flash('Your password must be greater than 8 characters', category='error')
    else:
        flash('Account Created!', category='success')
    return render_template("sign_up.html")


@app.route('/logout')
def logout():
    """ """
    return render_template("logout.html")


if __name__ == "__main__":
    create_database()
    app.run(debug=True)

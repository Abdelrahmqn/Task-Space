#!/usr/bin/python3
""" """
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy.sql import func


db = SQLAlchemy()
NAME = "datab.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{NAME}'
db.init_app(app)


def create_database():
    """ """
    if not path.exists(NAME):
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
@app.route('/home')
def home_page():
    """ """
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    """ """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            flash('logged in!', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('login error, try again.', category='error')
    return render_template("login.html", boolean=True)


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """ """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        
        if not first_name:
            flash('First name is required', category='error')
        elif len(first_name) < 2:
            flash('Your first name must be greater than 2 characters', category='error')
        elif not password:
            flash('Password is required', category='error')
        elif password != password2:
            flash('Your passwords don\'t match', category='error')
        elif len(password) < 8:
            flash('Your password must be greater than 8 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('home_page'))
    return render_template("sign_up.html")


@app.route('/logout')
@login_required
def logout():
    """ """
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('home_page'))


if __name__ == "__main__":
    create_database()
    app.run(debug=True)

from flask import render_template, redirect, url_for, flash
from my_app.forms import SignUp, Login
from my_app import app

@app.route('/')
@app.route('/home')
def home():
    """
    Renders the home template if the user is authenticated.
    Redirects to a login page if the user is not authenticated.
    """
    return render_template("home.html")

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Sign Up', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', title='Login', form=form)
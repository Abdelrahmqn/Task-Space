from flask import render_template, redirect, url_for, flash, Blueprint
from my_app.forms import SignUp, Login

auth = Blueprint('auth', __name__)
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='Sign Up', form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
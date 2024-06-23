#!/usr/bin/python3
""" """

from flask import Blueprint, render_template

view = Blueprint('view', __name__)

@view.route('/')
def home_page():
    return render_template("home.html") # sure will home.html exist.


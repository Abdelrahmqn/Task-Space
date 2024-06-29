from flask_login import UserMixin
from sqlalchemy.sql import func
from my_app import db



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
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150))
	username = db.Column(db.String(20), unique=True)	
	password = db.Column(db.String(100))
	posts = db.relationship('Post')

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	description = db.Column(db.String(10000))
	link = db.Column(db.String(10000))
	time = db.Column(db.DateTime(timezone=True), default = func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
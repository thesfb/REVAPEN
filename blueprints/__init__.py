from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def makeApp():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'qwerty'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)



	from .core import core
	from .auth import auth
	from .create import create

	app.register_blueprint(core, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')
	app.register_blueprint(create, url_prefix='/')

	from .models import User, Post

	with app.app_context():
		db.create_all()

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))
	

	return app



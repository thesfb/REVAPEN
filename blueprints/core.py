from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Post
from . import db
from flask.cli import with_appcontext

core = Blueprint('core',__name__,template_folder='templates',static_folder='static')

@core.route('/')
def home():
	
	return render_template('home.html', user=current_user,posts=Post.query.order_by(Post.id.desc()).all())


from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, login_user, logout_user, current_user


auth = Blueprint('auth',__name__,template_folder='templates',static_folder='static')

@auth.route('/login', methods=['GET','POST'])
def login():
	if request.method=='POST':
		username = request.form.get('username')
		password  =request.form.get('password')

		user = User.query.filter_by(username=username).first()
		if user:
			if check_password_hash(user.password,password):
				flash('Logged in successfully', category ='success')
				login_user(user, remember = True)
				return redirect(url_for('core.home'))
			else:
				flash('Incorrect password!', category = 'error')
		else:
			flash('Username does not exits!!', category='error')

	
	return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required 
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':
		name = request.form.get('name')
		username = request.form.get('username')
		password = request.form.get('password')

		user = User.query.filter_by(username=username).first()

		if user:
			flash("Username already exists!!", category='error')

		if len(username)<6:
			flash("Username must be more than 6 characters", category='error')
		if len(password)<8:
			flash("Password must be more than 8 characters", category='error')
		else:
			new_user = User(name=name,username=username, password=generate_password_hash(password))
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember = True)
			flash("Account created successfully", category='success')

			return redirect(url_for('core.home'))


	return render_template('signup.html', user = current_user)


@login_required
@auth.route('/myPosts')
def home():
	
	return render_template('userposts.html', user=current_user)


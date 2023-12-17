from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import Post
from . import db
import json

create = Blueprint('create',__name__,template_folder='templates',static_folder='static')



@create.route('/addProject', methods=['POST','GET'])
@login_required
def addProject():
	if request.method == 'POST':
		title = request.form.get('title')
		desc = request.form.get('description')
		link = request.form.get('link')

		new_post = Post(title=title, description=desc,link=link, user_id = current_user.id)
		db.session.add(new_post)
		db.session.commit()


	return render_template('create.html', user=current_user)


@create.route('/delete-post', methods=['POST'])
def delete_post():
	post = json.loads(request.data)
	postId = post['postId']
	post = Post.query.get(postId)
	if post:
		if post.user_id == current_user.id:
			db.session.delete(post)
			db.session.commit()
	
	return jsonify({})







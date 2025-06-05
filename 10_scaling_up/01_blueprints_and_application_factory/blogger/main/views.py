from flask import session, redirect, url_for, render_template, flash
from . import main
from .. models import User, Post, db
from .. forms import AboutUserForm

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about_user')
def about_user():
    aboutuserform = AboutUserForm()
    if session['user_available']:
        user = User.query.filter_by(username=session['current_user']).first()
        return render_template('about_user.html', user=user, aboutuserform=aboutuserform)
    flash('You are not a Authenticated User')
    return redirect(url_for('main.index'))
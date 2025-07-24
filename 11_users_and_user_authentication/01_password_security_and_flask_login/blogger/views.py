from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from flask_login import logout_user, login_user, login_required, current_user

from . models import User, Post, db
from . forms import AddPostForm, SignUpForm, SignInForm, AboutUserForm

from blogger import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
@login_required
def show_posts():
    posts = Post.query.all()
    user = User.query.all()
    return render_template('posts.html', posts=posts, user=user)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    blogpost = AddPostForm(request.form)
    us = User.query.filter_by(username=session['current_user']).first()
    if request.method == 'POST':
        bp = Post(blogpost.title.data, blogpost.description.data, us.uid)
        db.session.add(bp)
        db.session.commit()
        return redirect(url_for('show_posts'))
    return render_template('add.html', blogpost=blogpost)


@app.route('/delete/<pid>/<post_owner>', methods=('GET', 'POST'))
def delete_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        db.session.delete(me)
        db.session.commit()
        return redirect(url_for('show_posts'))
    flash('You are not a valid user to Delete this Post')
    return redirect(url_for('show_posts'))


@app.route('/update/<pid>/<post_owner>', methods=('GET', 'POST'))
def update_post(pid, post_owner):
    if session['current_user'] == post_owner:
        me = Post.query.get(pid)
        blogpost = AddPostForm(obj=me)
        if request.method == 'POST':
            bpost = Post.query.get(pid)
            bpost.title = blogpost.title.data
            bpost.description = blogpost.description.data
            db.session.commit()
            return redirect(url_for('show_posts'))
        return render_template('update.html', blogpost=blogpost)
    flash('You are not a valid user to Edit this Post')
    return redirect(url_for('show_posts'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        reg = User(signupform.firstname.data, signupform.lastname.data,\
         signupform.username.data, signupform.password.data,\
         signupform.email.data)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', signupform=signupform)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()
    if signinform.validate_on_submit():
        print('llll')
        user = User.query.filter_by(email=signinform.email.data).first()
        print(user, signinform.password.data)

        if user and user.verify_password(signinform.password.data):
            login_user(user, remember=signinform.remember_me.data)
            print('Login successful!')
            flash('Login successful!', 'success')
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        else:
            flash('Invalid email or password', 'error')
    return render_template('signin.html', signinform=signinform)


@app.route('/about_user')
@login_required
def about_user():
    aboutuserform = AboutUserForm()
    user = User.query.filter_by(username=session['current_user']).first()
    return render_template('about_user.html', user=user, aboutuserform=aboutuserform)


@app.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out successfully")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

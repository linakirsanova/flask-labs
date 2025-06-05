from flask import request, session, redirect, url_for, render_template
from . import auth
from .. models import User, db
from .. forms import SignUpForm, SignInForm

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignUpForm(request.form)
    if request.method == 'POST':
        reg = User(signupform.firstname.data, signupform.lastname.data,\
         signupform.username.data, signupform.password.data,\
         signupform.email.data)
        db.session.add(reg)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('signup.html', signupform=signupform)


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    signinform = SignInForm()
    if request.method == 'POST':
        em = signinform.email.data
        log = User.query.filter_by(email=em).first()
        if log.password == signinform.password.data:
            current_user = log.username
            session['current_user'] = current_user
            session['user_available'] = True
            return redirect(url_for('blog.show_posts'))
    return render_template('signin.html', signinform=signinform)

@auth.route('/logout')
def logout():
    session.clear()
    session['user_available'] = False
    return redirect(url_for('main.index'))

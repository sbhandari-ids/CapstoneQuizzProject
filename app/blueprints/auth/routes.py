from flask import flash, redirect, render_template, request, url_for
from . import auth
from app.blueprints.auth.forms import LoginForm, SignUpForm
from app.models import Course, User, db
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash 


# @auth.route('/')
# def home():
#    return render_template('home.html')

@auth.route('/login', methods = ['GET','POST'])
def login():
    #loginForm = LoginForm()
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            flash(f'Welcome {queried_user.username}!', 'info')
            login_user(queried_user)
        # flash('Login Successful !', 'info')
            return redirect(url_for('main.home'))
        else: 
            flash('Invalid user email or password', 'warning')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    #signUpForm = signUpForm()
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data 
        new_user = User(username,email, password)
        new_user.save()
        flash('Success ! Thank you for Signing up with Theives !', 'success')
        return redirect(url_for('auth.login')) #login here is the function name for Login, not the route '/login'
    else:
        return render_template('signup.html', form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
  


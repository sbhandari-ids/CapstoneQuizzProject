# from flask import render_template
# from app import app

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/login', methods = ['GET','POST'])
# def login():
#     #loginForm = LoginForm()
#     form = LoginForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#         return f'{email} {password}'
#     return render_template('login.html', form=form)

# @app.route('/signup', methods = ['GET','POST'])
# def signup():
#     #signUpForm = signUpForm()
#     form = SignUpForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         username = form.username.data
#         email = form.email.data
#         password = form.password.data 
#         return f'{username} {email} {password}'
#     return render_template('signup.html', form=form)
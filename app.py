from flask import Flask, render_template, request
import requests
# import jsonify
# from flask.ext.bcrypt import Bcrypt
# from init import botstart
# from flask_login import LoginManager,login_user
# from controllers import *
# login_manager = LoginManager()
app = Flask(__name__, static_folder='static', static_url_path='/static')
# login_manager.init_app(app)
# Bcrypt Config
# from config import *
# from models import *
# app.config['SQLALCHEMY_DATABASE_URI'] = DB
# app.config['SECRET_KEY'] = '769876tr8629r9yog^%&^*)&*^%&()'
# #
# login_manager.login_view = '/signin'
# # from controllers import *
# # DB instance init
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# @login_manager.user_loader
# def load_user(id):
#     '''User Loader for flask-login
#     :params
#      user_id -> email
#     '''
#     user = User.query.get(id)
#     if user:
#         return user
#     else:
#         return None
# def commit(obj):
# 	if type(obj) == list:
# 		for i in obj:
# 			db.session.add(i)
# 		db.session.commit()
# 	else:
# 		db.session.add(obj)
# 		db.session.commit()
#

@app.route('/')
def index():
    #
    # page = requests.get("http://google.com")
    # page.status_code
    # soup = BeautifulSoup(page.content, 'html.parser')
    # soup.find_all(id="lga")

    return render_template('public/index.html')


@app.route('/signin', methods=['POST', 'GET'])
def index1():
    if request.method == 'GET':
        return render_template('public/signin.html')

    # if request.method == 'POST':
    #
    #     params = request.form
    #     username = params['username']
    #     password = params['password']
    #     print password
    #     user = 'nav'
    #     user = User.query.filter_by(username=username)
    #     user = user.first()
    #             # password = User.query.filter_by(password=password)
    #     # # user = user.first()
    #     # registered_user = User.query.filter_by(username=username,password=password).first()
    #     # if registered_user is None:
    #     #     flash('Username or Password is invalid' , 'error')
    #     # return redirect(url_for('login'))
    #     # login_user(registered_user)
    #     # flash('Logged in successfully')
    #     # return redirect(request.args.get('next') or url_for('index'))
    #     if 'remember' in params:
    #         remember = True
    #
    #     if user:
    #         print 'asasas'
    #         # return render_template('public/trynow.html')
    #
    #         if user.is_password_correct(password):
    #             login_user(user)
    #             user.authenticated = True
    #             # db.session.add(user)
    #             # db.session.commit()
    #             return render_template('public/trynow.html')
    #

        # return render_template('public/signin.html',fail=True)
        #
        #

@app.route('/admin')
def admin():
    if request.method == 'GET':
        return render_template('admin_boostlikes/index.html')
        # admin
        # admin


@app.route('/signup', methods=['POST','GET'])
def index2():

    if request.method == 'GET':
        return render_template('public/signup.html')
    #
    #
    # if request.method == 'POST':
    #     login_manager.login_view = '/signup'
    #
    #     params = request.form
    #     username = params['username']
    #     password = params['password']
    #     email = params['email']
    #     user = User()
    #     user.username = username
    #     user.password = password
    #     user.email = email
    #     db.session.add(user)
    #     db.session.commit()
    #     return render_template('public/index.html')
    #     # return render_template('public/trynow.html')
    #

@app.route('/trynow')
def trynow():
    if request.method == 'GET':
        return render_template('public/trynow.html')
        #


@app.route('/home')
def indexhome():
    if request.method == 'GET':
        return render_template('adminm/home.html')
        #


@app.route('/about')
def indexabout():
    if request.method == 'GET':
        return render_template('public/about.html')


@app.route('/Boost')
def index3():
    if request.method == 'GET':
        return render_template('admin_boostlikes/Boost.html')


@app.route('/Listlike')
def index4():
    if request.method == 'GET':
        return render_template('admin_boostlikes/Listlike.html')
        #


@app.route('/dashboard')
def index5():
    if request.method == 'GET':
        return render_template('admin_boostlikes/index.html')
        #


@app.route('/AutoRound', methods=['POST', 'GET'])
def index6():
    if request.method == 'GET':
        return render_template('admin_boostlikes/autoround.html')
    if request.method == 'POST':
           #  engine.index6()
        return render_template('admin_boostlikes/autoround.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8002, debug=True, threaded=True)

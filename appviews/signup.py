from flask import Blueprint
from flask import  render_template, g
# from flask_login import LoginManager, login_user, logout_user
from flask_login import logout_user, login_required, UserMixin
import flask_login
from controller import controller

from controller.controller import gen
from flask import render_template, request
print controller.gen()
# login_manager.session_protection = "strong"
from config import *

signup = Blueprint('signup', __name__)
from models.Usermodel import *
from approutes import my_view
from app import db
@my_view.route ('/signup', methods=['POST', 'GET'])
def index2():

    if request.method == 'GET':
        return render_template ('public/signup.html')

    if request.method == 'POST':
        # login_manager.login_view = '/signup'

        params = request.form
        username = params['username']
        password = params['password']
        email = params['email']

        user = db.session.query (User).filter (User.username == username).first ()
        emailusr = db.session.query (User).filter (User.email == email).first ()
        print (user)
        if user:
            return render_template ('public/signup.html')

        if emailusr:
            return render_template ('public/signup.html')

        else:
            try:
                password = bcrypt.generate_password_hash (password)
                # print password
                user = User()
                user.username = username
                user._password = password
                user.email = email

                db.session.add (user)

                db.session.commit()

                # text = text1 + make_footer (username, password, email)
                # send_mail (username, text)

                print (user._password)
                print (user.email)
                return render_template ('public/signin.html')

            except:
                return render_template ('public/signup.html')

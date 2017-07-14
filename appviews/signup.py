from flask import Blueprint
from flask import  render_template, g
# from flask_login import LoginManager, login_user, logout_user
from flask_login import logout_user, login_required, UserMixin
import flask_login
from controller import controller
# import bcrypt
from controller.controller import gen
from flask import render_template, request
print controller.gen()
# login_manager.session_protection = "strong"
from config import *
import models
from app import bcrypt
signup = Blueprint('signup', __name__)

from approutes import my_view
from app import db
# from models.Usermodel import

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

        user = models.Usermodel.User.query.filter(models.Usermodel.User.username == username).first ()
        email = models.Usermodel.User.query.filter(models.Usermodel.User.email == email).first ()
        print user
        if user!=None:
            return render_template ('public/signup.html')
        if email!= None:
            return render_template ('public/signup.html')

        if user == None:
            if email == None:
                password = bcrypt.generate_password_hash(password)
                # print password
                user = models.Usermodel.User()
                user.username = username
                user._password = password
                user.email = email

                db.session.add (user)

                db.session.commit()

                # text = text1 + make_footer (username, password, email)
                # send_mail (username, text)

                return render_template ('public/signin.html')


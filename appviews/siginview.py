
import flask
import sys
from flask import render_template, request
from flask import Blueprint
from flask_login import login_required,login_user
# from flask import  render_template, g
# from flask_login import LoginManager, login_user, logout_user
from flask_login import logout_user, login_required, UserMixin
import flask_login
from controller import controller
from controller.controller import gen
#login_manager.session_protection = "strong"
from app import db
import models
userdatastore=None

# signin = Blueprint('signin',__name__)
from approutes import my_view
# from model import db
# from model import *
# from models.Usermodel import User
@my_view.route ('/signin', methods=['POST', 'GET'])
def verify_user_password():
    if request.method == 'GET':
        # logout_user(user)
        return render_template ('public/signin.html')

    if request.method == 'POST':
        params = request.form
        # print params
        username = params['username']
        password = params['password'].encode ('utf-8')
        remember = False
        user =models.Usermodel.User.query.filter_by (username=username)
        user = user.first ()

        if user:
            if user.is_password_correct (password):

                login_user (user)
                user.authenticated = True
                user.is_anonymous ()
                #
                flask.flash ('Logged in successfully.')

                next = flask.request.args.get ('next')
                # t=[]
                t = [user.username]
                global userdatastore
                userdatastore = t
                db.session.permanent = True
                print userdatastore

                global userisauth



                userisauth = True

                # is_safe_url should check if the url is safe for redirects.
                # See http://flask.pocoo.org/snippets/62/ for an example.


                return flask.redirect (next or flask.url_for ('my_view.dashboard'))
            else:
                return flask.render_template ('public/signin.html')
        else:
            return flask.render_template ('public/signin.html')

@my_view.before_request
def before_request():
     import datetime
     flask.session.permanent = True
     my_view.permanent_session_lifetime = datetime.timedelta(seconds=30)
     flask.session.modified = True

def getusername():
    global userdatastore
    return userdatastore

import flask
import sys
from flask import Blueprint
from flask_login import login_required,login_user
# from flask import  render_template, g
# from flask_login import LoginManager, login_user, logout_user
from flask_login import logout_user, login_required, UserMixin
import flask_login
from controller import controller
from controller.controller import gen
# from app import *
from flask import render_template, request
# print controller.gen()
# login_manager.session_protection = "strong"
from config import *


signin = Blueprint('signin', __name__)
from model import *


@signin.route ('/signin', methods=['POST', 'GET'])
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

        if 'remember' in params:
            remember = True

        # user = db.session.query(User).filter(User.username==username).first()
        user = User.query.filter_by (username=username)
        user = user.first ()

        if user:
            if user.is_password_correct (password):

                login_user(user)
                user.authenticated = True
                user.is_anonymous ()
                #
                flask.flash ('Logged in successfully.')

                next = flask.request.args.get ('next')
                # t=[]
                t = [user.username]
                global userdatastore
                userdatastore = t
                global userisauth
                userisauth = True
                # is_safe_url should check if the url is safe for redirects.
                # See http://flask.pocoo.org/snippets/62/ for an example.


                return flask.redirect (next or flask.url_for ('my_view.dashboard'))
            else:
                return flask.render_template ('public/signin.html')
        else:
            return flask.render_template ('public/signin.html')


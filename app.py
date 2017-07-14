
#Author: Navjot singh Babrah
import os
import re
import user


import flask
from flask import Flask, Blueprint, render_template, request, jsonify, g, make_response, redirect, url_for, session, \
    send_from_directory
from paypalrestsdk import Payment
import requests

from sqlalchemy import update


# from appviews.siginview import my_view
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, login_required, UserMixin,LoginManager

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
# import flask_sqlalchemy
from paypalrestsdk import Payment
import logging
import json

from paypalrestsdk import BillingPlan, BillingAgreement
from flask_bcrypt import Bcrypt

import paypalrestsdk
import flask_login


from config import *
from OpenSSL import SSL

from controller import controller
# from flask_restful import Api

URL = 'https://api.mailgun.net/v3/sandbox047085ca4cac4999b35d70a3e5be1c30.mailgun.org'
MAILGUN_API_KEY = 'key-ac15a94e886e6bc11d0886c4192d4536'
d = '/static'
login_manager = LoginManager()

app = Flask (__name__)

login_manager.init_app (app)

app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SECRET_KEY'] = '769876tr8629r9yog^%&^*13*^&)&*^%&()'
# the payment transaction description."}]})
# login_manager.anonymous_user =''
app.config['CONTENT_DIR'] = d
login_manager.login_view = 'signin'
login_manager.session_protection = "strong"
# from controllers import *
# DB instance init
db = SQLAlchemy (app)
bcrypt = Bcrypt (app)
# api = Api(app)
SECRET_KEY = '$&^&B&*^*MN&*CDMN&*()B^&*()P^&_N*NM(P)*&D()&*^'
my_api = paypalrestsdk.configure ({
    "mode": "live",  # sandbox or live
    "client_id": "Aco9MZMq14DP2vfkP1xJRLkxtnwHRdxUobFUSeo15r3bKlDqT1K1sLGIR7t12s4DP5kmCTm5WZFoTR4O",
    "client_secret": "EDi6nGy_SGgVgEul9uPW3WxSXhIugIwn4MYrfkowdx13TcXMh87uU3wTkb3bhRIvmWMZT8esA1VZhh7G"})
my_api.get_access_token ()
logging.basicConfig (level=logging.INFO)
    # return 'http://0.0.0.0:2300/'
from appviews.approutes import my_view
from appviews.siginview import signin
from appviews.signup import signup

from appviews.dashboard import dashboard
from appviews.signup import index2
from appviews.trynow import trynow
from appviews.ManageAccount import manage
userdatastore = None
userisauth = None
billing_id = None

from appviews.changeAccountname import changeAccountname
from appviews.paypalAutoround import startpaypal,subscribe
from appviews.userauth import userauth
# from model import *
from models.Usermodel import *
app.register_blueprint(my_view)

# app.register_blueprint(dashboard)
# from paymnts import *
def commit(obj):
    if type (obj) == list:
        for i in obj:
            db.session.add (i)
        db.session.commit ()
    else:
        db.session.add (obj)
        db.session.commit ()




@login_manager.user_loader
def load_user(user_id):
    '''User Loader for flask-login
    :params
     user_id -> email
    '''
    user = User.query.get (user_id)
    if user:
        return user
    else:
        return None


if __name__ == '__main__':
    app.run (host='0.0.0.0',debug=True,port=5300)

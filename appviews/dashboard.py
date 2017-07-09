from flask import Blueprint
from flask import  render_template, g
# from flask_login import LoginManager, login_user, logout_user
from flask_login import logout_user, login_required, UserMixin
import flask_login
from controller import controller
from controller.controller import gen
# from app import *
from flask import render_template, request
print controller.gen()
# login_manager.session_protection = "strong"
from config import *


dashboard = Blueprint('dashboard', __name__)


@dashboard.route ('/home#', methods=['GET', 'POST'])
# @cross_origin()
# @auth.verify_password
@login_required

def dashboard():
    if request.method == 'GET':


        return render_template ('public/test1.html')
    else:
        return render_template ('public/signin.html')



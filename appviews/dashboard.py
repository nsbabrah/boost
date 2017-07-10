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
from approutes import my_view
d = Blueprint('d', __name__)


@my_view.route ('/dashboard', methods=['POST', 'GET'])
@login_required
def dashboard():
    if request.method == 'GET':
        return render_template('public/test1.html')
        # logout_user(user)

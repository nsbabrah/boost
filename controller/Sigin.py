
import flask
import sys

from flask import Blueprint

import controller

from flask import render_template, request
print controller.gen()
from flask_login import logout_user, login_user,login_required, UserMixin
import flask_login
from appviews.approutes import my_view
from models import *

from models.Usermodel import *
def usersignin(username,password):




    # user = db.session.query(User).filter(User.username==username).first()
    user = User.query.filter_by (username=username)
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
            global userisauth
            userisauth = True



            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.


            return flask.redirect(next or flask.url_for ('my_view.dashboard'))
        else:
            return flask.render_template ('public/signin.html')
    else:
        return flask.render_template ('public/signin.html')

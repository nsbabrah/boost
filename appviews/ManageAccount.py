

from app import db,bcrypt

import paypalrestsdk
import flask_login

from config import *
from OpenSSL import SSL
from flask import request,render_template,redirect,url_for
from approutes import my_view
# from flask import render_template,request
import models

useraccname=0
from userauth import storename
@my_view.route ('/manage', methods=['POST', 'GET'])
def manage():
    if request.method == 'POST':
        global useraccname

        print request.json
        global useraccname
        useraccname = 'pavi'
        print str(useraccname)
        userchangevalue=request.json['value']
        changewhat=request.json['change']
        print userchangevalue,changewhat

        if(changewhat=='Username'):

            user = models.Usermodel.User.query.filter(models.Usermodel.User.username == userchangevalue).first ()

            print user
            if user != None:
                return "False User Already Register"
            if user == None:
                    user = models.Usermodel.User.query.filter_by (username=useraccname).first()
                    user.username = userchangevalue
                    db.session.add (user)
                    db.session.commit ()
                    return 'True'

        elif(changewhat=='Email'):
            email = models.Usermodel.User.query.filter(models.Usermodel.User.email == userchangevalue).first ()
            if email != None:
              return 'email already register'
            elif email == None:
                user = models.Usermodel.User.query.filter_by (username=useraccname).first ()
                user.email = userchangevalue
                db.session.add(user)
                db.session.commit()
                print 'email'
        elif(changewhat=='Password'):
                user = models.Usermodel.User.query.filter_by (username=useraccname).first ()
                user._password = bcrypt.generate_password_hash(userchangevalue)
                db.session.add(user)
                db.session.commit()
                print 'Pass'

                return 'True'



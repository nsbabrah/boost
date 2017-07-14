

from app import db

import paypalrestsdk
import flask_login

from config import *
from OpenSSL import SSL
from flask import request
from approutes import my_view

import models

useraccname=0
from userauth import storename
from siginview import getusername
@my_view.route ('/manage', methods=['POST', 'GET'])
def manage():
    if request.method == 'POST':
        global useraccname

        print request.json
        global useraccname
        useraccname = getusername()
        print str(useraccname)
        userchangevalue=request.json['value']
        changewhat=request.json['change']
        print userchangevalue,changewhat

        if(changewhat=='Username'):
            user = models.Usermodel.User.query.filter_by (username= useraccname).first ()
            user.username = userchangevalue
            db.session.add (user)
            db.session.commit()
            user = models.Usermodel.userpackage.query.filter_by (username=useraccname).first ()
            user.username = userchangevalue
            db.session.add (user)
            db.session.commit ()

            print 'username'

        elif(changewhat=='Email'):
            user = models.Usermodel.User.query.filter_by (username=userchangevalue).first ()
            user.username = userchangevalue
            db.session.add(user)
            db.session.commit()
            print 'email'
        elif(changewhat=='Password'):
            user = models.Usermodel.User.query.filter_by (username=userchangevalue).first ()
            user.username = userchangevalue
            db.session.add(user)
            db.session.commit()
            print 'Pass'

        return True



from approutes import my_view
from flask import request
from flask import jsonify
from flask_login import current_user
import flask_login
from controller.Bot import lumi
from app import db
import models
import json

@my_view.route('/listlikeinfo',methods=['GET'])
def listlikeinfo():

    r = ['redtu', 'topa', 'nehala', 'bc']
    return json.dumps(r)

@my_view.route('/startlistlike',methods=['POST'])
def startlistlikes():

    user=[]
    username=flask_login.current_user
    accname=[]
    password=[]


    lumi.userprofile_start(username,accname,password)

    return 'START'



@my_view.route('/changeActiveUser',methods=['POST'])
def listlike_changename():
    changeusername = request.json
    changeusername =request.json['new_active_user']
    old_name = request.json['old_active_user']
    username=flask_login.current_user
    print changeusername

    user = db.session.query(models.Usermodel.Listlikes.username,models.Usermodel.Listlikes.email).filter(models.Usermodel.Listlikes.username== username).all()
    if user == None:
        return 'User have no account'
    if user!=None:
        userch = db.session.query(models.Usermodel.Listlikes.username,models.Usermodel.Listlikes.email).filter(models.Usermodel.Listlikes.instauser == changeusername).all()
        if userch == None:
            return 'You dont have any account'
        if userch != None:
            userdata = models.Usermodel.Listlikes.query.filter_by(instauser=old_name).first()
            userdata.listlikestatus = '0'

            userdata = models.Usermodel.Listlikes.query.filter_by (instauser=changeusername).first()
            userdata.listlikestatus = '1'

            db.session.add (userdata)
            db.session.commit()

            return 'True'



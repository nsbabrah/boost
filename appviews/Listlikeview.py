from approutes import my_view
from flask import request
from flask import jsonify
from flask_login import current_user
import flask_login
from controller.Bot import lumi
from models import listlike
import models
from models.listlike import db
import json

@my_view.route('/listlikeinfo',methods=['GET'])
def listlikeinfo():

    user=flask_login.current_user
    t=[]
    user=user.username
    uslistlikes= db.session.query(models.listlike.Listlikes.instauser).filter(models.listlike.Listlikes.user ==  user).all()
    active_user = db.session.query(models.listlike.Listlikes.instauser).filter(models.listlike.Listlikes.listlikestatus ==1,models.listlike.Listlikes.user ==  user).all()
    print active_user

    for i in uslistlikes:
        t.append (list (i))



    print sum(t, [])

    return jsonify({'data':sum(t, []),'active_user':str(active_user[0][0])})

@my_view.route('/startlistlike',methods=['POST'])
def startlistlikes():

    targets=request.json
    username=flask_login.current_user
    print (targets)
    print u", ".join(targets['users'])
    accname=[]
    password=[]
    user = username.username
    #here u need to check which user from this boostlike user have listlikestatus one send him to bot func
    return 'START'


    # user = db.session.query(models.listlike.Listlikes.user).filter (models.listlike.Listlikes.user == username).all ()
    # if user!=None:
    #     user = db.session.query (models.listlike.Listlikes.instauser,models.listlike.Listlikes.instapass).filter( models.listlike.Listlikes.user == user).all ()
    #     print user
    #
    #
    #
    #     lumi.userprofile_start()
@my_view.route('/changeActiveUser',methods=['POST'])
def listlike_changename():
    changeusername = request.json
    changeusername =request.json['new_active_user']
    old_name = request.json['old_active_user']
    username=flask_login.current_user
    print changeusername






    if len(old_name) == 0:
        userdata = models.listlike.Listlikes.query.filter_by (instauser=changeusername).first ()
        userdata.listlikestatus = '1'

        db.session.add (userdata)
        db.session.commit ()
        return 'True'

    elif len(old_name)!=0:
            try:

                userdata = models.listlike.Listlikes.query.filter_by(instauser=old_name).first()
                userdata.listlikestatus = '0'


                userdata = models.listlike.Listlikes.query.filter_by (instauser=changeusername).first()
                userdata.listlikestatus = '1'

                db.session.add (userdata)
                db.session.commit()
            except:
                db.session.rollback()
            return 'True'



@my_view.route('/changeInstaData',methods=['POST'])
def listlike_INsta_data():
    changeusername = request.json

    username=flask_login.current_user
    print changeusername
    newinsta_user=request.json['insta_username']
    newinsta_pass=request.json['insta_password']
    us = db.session.query(models.listlike.Listlikes.user).filter(models.listlike.Listlikes.user == username.username).all ()
    if us!=None:
        userdata = models.listlike.Listlikes.query.filter_by (listlikestatus='1').first ()
        userdata.instauser = newinsta_user
        userdata.instapass = newinsta_pass
        db.session.add (userdata)
        db.session.commit ()
        return 'True'
    # if user == None:
    #     return 'User have no account'
    # if user!=None:
    #     userdata = models.Usermodel.userpackage.query.filter_by (instauser=newinsta_pass).first ()
    #     userdata.Auto_ac_name = useraccname
    #     db.session.add (userdata)
    #     db.session.commit ()
    #     print "payemt done"

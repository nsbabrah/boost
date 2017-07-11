from flask import Blueprint
import flask
from approutes import my_view
# from models.Usermodel import *
import json
from app import db
from flask import render_template, request
from sqlalchemy import update
import models

@my_view.route ('/userauth', methods=['GET'])
def userauth():
    if request.method == 'GET':
        # username = request.get_json()

        us = 'nav'
        # if userisauth and userdatastore is not None:
        user = db.session.query (models.Usermodel.userpackage.username, models.Usermodel.userpackage.Auto_ac_name,models.Usermodel.userpackage.Listlikepackage,
                                 models.Usermodel.userpackage.usr_id,models.Usermodel.userpackage.Auto_round_state).filter (models.Usermodel.userpackage.username == us).all ()

        t = []
        col = ["username", "Auto_ac_name", "listlike", "usr_id","play"]

        for i in user:
            t.append (list (i))

        temp = []
        for i in t:
            temp.append (dict (zip (col, i)))
        print (temp)
        return json.dumps (temp)
    else:
        return {'auth': "false"}



@my_view.route ('/changeState', methods=['POST'])
def changeaccountstate():
    if request.method == 'POST':
        # username = request.get_json()


        params = request.json
        print params
        state = params['state']
        name = params['name']
        # if userisauth and userdatastore is not None:

        rows_changed = update(models.Usermodel.userpackage).where(models.Usermodel.userpackage.Auto_ac_name == name).values(Auto_round_state = state )
        # rows_changed.Auto_round_state = state

        db.session.commit()
        return "BNPBArdhan"

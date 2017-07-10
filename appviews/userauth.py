
from approutes import my_view
from models.Usermodel import *
import json
from app import db
from flask import render_template, request

@my_view.route ('/userauth', methods=['GET'])
def userauth():
    if request.method == 'GET':
        # username = request.get_json()

        us = 'nav'
        # if userisauth and userdatastore is not None:
        user = db.session.query (userpackage.username, userpackage.Auto_ac_name, userpackage.Listlikepackage,
                                 userpackage.usr_id).filter (userpackage.username == us).all ()

        t = []
        col = ["username", "Auto_ac_name", "listlike", "usr_id"]

        for i in user:
            t.append (list (i))

        temp = []
        for i in t:
            temp.append (dict (zip (col, i)))
        print (temp)
        return json.dumps (temp)
    else:
        return {'auth': "false"}
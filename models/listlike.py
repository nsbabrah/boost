from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from config import *
from app import db,bcrypt,UserMixin

from sqlalchemy.ext.hybrid import hybrid_property
#from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
#
#

class userpackage_listlike(db.Model):
    # __bind_key__ = 'local'
    __tablename__ = "userpackage"

    usr_id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    username = db.Column(db.String(255))
    # last_name = db.Column(db.String(254))
    # access = db.Column(db.String(254))
    # status = db.Column(db.String(255))
    usr_email = db.Column(db.String(255), unique=True)
    Auto_ac_name = db.Column (db.String (255))

    Auto_round_state = db.Column (db.BOOLEAN (200))





    def get_id(self):
        return unicode(self.username)

    # def __init__(self, username,Auto_ac_name):
    #     self.username = username
    #     self.Auto_ac_name= Auto_ac_name
        # self._password = password

    def user_data(self):
        # for i in package1:
            return [{"username":self.username,"package1":self.Auto_ac_name,"id":self.usr_id},]


    def __repr__(self):
        return '{}'.format(self.username,self.Auto_ac_name,self.Listlikepackage)


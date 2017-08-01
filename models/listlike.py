
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from config import *
from app import db,bcrypt,UserMixin

from sqlalchemy.ext.hybrid import hybrid_property
#from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
#
class Listlikes(db.Model):



    usr_id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    user = db.Column(db.String(255))

    listlikestatus = db.Column (db.String (255))

    instauser = db.Column (db.String (200))
    instapass = db.Column (db.String (200))




    def __repr__(self):
        return 'Listlikes :{}'.format(self.username,self.instauser,self.instapass,self.listlikestatus)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from app import db,bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class Userpayemt(db.Model):
	# __bind_key__ = 'local'
    # __tablename__ = ""

	usr_id = db.Column(db.Integer, primary_key = True, autoincrement =True)
	username = db.Column(db.String(254))
	# last_name = db.Column(db.String(254))
	access = db.Column(db.String(254))
    status = db.Column(db.String(254))
	email = db.Column(db.String(254), unique=True)




	# Flag for session management
	authenticated = db.Column(db.Boolean, default=False)

	#Flag for email verification
	email_confirmed = db.Column(db.Boolean, default=False)
    

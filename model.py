from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from config import *
from app import db,bcrypt,UserMixin,auth
from sqlalchemy.ext.hybrid import hybrid_property
#from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
#
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://boostlikes@localhost/Boostlikes'
# app.config['SECRET_KEY'] = 'super-secret'
# app.config['SECURITY_REGISTERABLE'] = True
#
# app.debug = True
# db = SQLAlchemy(app)

# engine = sqlalchemy.create_engine('mysql+mysqldb://boostlikes:boostlikes@localhost/STUDENT')
# Session =  scoped_session(sessionmaker(bind=engine))

# s = Session()
# result = s.execute('SELECT * FROM STUDENT;')
# print result

class User1(db.Model):
    __tablename__ = "user-assigned"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    # email = db.Column('email',db.String(50),unique=True , index=True)
    # registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
    def add(self , username ,password , email):
        self.username = username
        self.password = password

        # add=


class User(db.Model,UserMixin):
    # __bind_key__ = 'local'
    __tablename__ = "user"


    user_id = db.Column(db.Integer, primary_key = True, autoincrement =True)

    username = db.Column (db.String (254))
    # last_name = db.Column(db.String(254))
    # access = db.Column (db.String (254))
    email = db.Column (db.String (254), unique=True)

    _password = db.Column (db.String (254))

    # def get_username(self,username):
    #     return unicode (self.username)

    # def verify_password(self,password):
    #     return  bcrypt.check_password_hash(self._password,password)
    #
    #


    # def __init__(self, username, password):
    #     self.username = username
    #     self._password = password

            # self._password = db.Column(db.String(254))

        # Flag for session management
    # def getuser(self):
    #     return

    @hybrid_property
    def password(self):
        return self._password

    # Hashing the password once and for all
    @password.setter
    def _set_password(self,plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    # Password Matching
    # @auth.is_password_correct
    def is_password_correct(self,plaintext):
        return bcrypt.check_password_hash(self._password,plaintext)

    # @auth.verify_password
    # def verify_password(self,password):
    #     user.verify_password (password):
    #         return False
    #     g.user = user
    #     print g.user
    #
    #     return True
    # def __init__(self, user_id):
    #     return self.user_id
        # return self.user_id



    def getuser(self):
        return [username,_password,email]

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.user_id)

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


    def __repr__(self):
        return 'User : {}'.format(self.username,self.user_id)


class Userpayment(db.Model):
    # __bind_key__ = 'local'
    # __tablename__ = ""

    usr_id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    username = db.Column(db.String(255))
    # last_name = db.Column(db.String(254))
    # access = db.Column(db.String(254))
    status = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return 'Userpayment : {}'.format(self.username)


class userpackage(db.Model):
    # __bind_key__ = 'local'
    __tablename__ = "userpackage"

    usr_id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    username = db.Column(db.String(255))
    # last_name = db.Column(db.String(254))
    # access = db.Column(db.String(254))
    # status = db.Column(db.String(255))
    usr_email = db.Column(db.String(255), unique=True)
    Auto_ac_name = db.Column (db.String (255))
    Listlikepackage = db.Column (db.String (255))

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


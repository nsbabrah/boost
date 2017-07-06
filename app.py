

# import SQLAlchemy as SQLAlchemy
import os
import re
import user

import flask
from flask import Flask, Blueprint, render_template, request, jsonify, g, make_response, redirect, url_for, session, \
    send_from_directory
from paypalrestsdk import Payment
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, login_required, UserMixin
from requests import auth

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
# import flask_sqlalchemy
from paypalrestsdk import Payment
import logging
import json
# import jsonify
from paypalrestsdk import BillingPlan, BillingAgreement
from flask_bcrypt import Bcrypt
# import bcrypt
# import Bcr
# from init import botstart
# from flask_cors import CORS, cross_origin
import paypalrestsdk
import flask_login
from flask_login import LoginManager, login_user, logout_user
# cors = CORS(app, resources={r"/test/*": {"origins": "*"}})
# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()
from OpenSSL import SSL

# from boost.model import  *
# from setuptools import setup
# setup(
#     name='models',
#     packages=['models'],
#     include_package_data=True,
#     install_requires=[
#         'flask',
#     ],
# )

# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('yourserver.key')
# context.use_certificate_file('yourserver.crt')
# from manage import User
URL = 'https://api.mailgun.net/v3/sandbox047085ca4cac4999b35d70a3e5be1c30.mailgun.org'
MAILGUN_API_KEY = 'key-ac15a94e886e6bc11d0886c4192d4536'
d = '/static'
login_manager = LoginManager ()
app = Flask (__name__)
login_manager.init_app (app)
# CORS(app)
# logging.getLogger('flask_cors').level = logging.DEBUG

# logging.getLogger('flask_cors').level = logging.DEBUG


# login_manager.session_protection = "strong"
from config import *

# from paymnts import *
app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SECRET_KEY'] = '769876tr8629r9yog^%&^*13*^&)&*^%&()'
# the payment transaction description."}]})
# login_manager.anonymous_user =''
app.config['CONTENT_DIR'] = d
login_manager.login_view = 'signin'
# from controllers import *
# DB instance init
db = SQLAlchemy (app)
bcrypt = Bcrypt (app)

SECRET_KEY = '$&^&B&*^*MN&*CDMN&*()B^&*()P^&_N*NM(P)*&D()&*^'
my_api = paypalrestsdk.configure ({
    "mode": "live",  # sandbox or live
    "client_id": "Aco9MZMq14DP2vfkP1xJRLkxtnwHRdxUobFUSeo15r3bKlDqT1K1sLGIR7t12s4DP5kmCTm5WZFoTR4O",
    "client_secret": "EDi6nGy_SGgVgEul9uPW3WxSXhIugIwn4MYrfkowdx13TcXMh87uU3wTkb3bhRIvmWMZT8esA1VZhh7G"})

my_api.get_access_token ()
userdatastore = None
userisauth = None
billing_id = None

logging.basicConfig (level=logging.INFO)
def commit(obj):
    if type (obj) == list:
        for i in obj:
            db.session.add (i)
        db.session.commit ()
    else:
        db.session.add (obj)
        db.session.commit ()


# from controll.controller import
from model import *


# from controllers import *
@login_manager.user_loader
def load_user(user_id):
    '''User Loader for flask-login
    :params
     user_id -> email
    '''
    user = User.query.get (user_id)
    if user:
        return user
    else:
        return None

    # @login_manager.user_loader
    # def load_user(user_id):
    #      user=User.query.get(user_id)
    #      return user
    #
    # admin = Blueprint('index', __name__, static_folder='/static/boost')
    #
    # # @app.route('/')
    # def index():
    #     f="/static/boost/index.html"
    #     return url_for('index')
    # return  flask.redirect (flask.url_for ('da'))
    # return redirect(url_for ('/static/boost/', filename='index.html'))
    #   return render_template ('public/index.html')


#     # return render_template('public/index.html')
# @app.route('/<path:path>')
# def static_proxy(path):
#   # send_static_file will guess the correct MIME type
#   return app.send_static_file(path)
@app.route ('/', methods=['POST', 'GET'])
def da():
    if request.method == 'GET':
        return render_template ('public/index.html')
        # logout_user(user)


@app.route ('/signin', methods=['POST', 'GET'])
def verify_user_password():
    if request.method == 'GET':
        # logout_user(user)


        return render_template ('public/signin.html')

    if request.method == 'POST':

        params = request.form
        # print params
        username = params['username']
        password = params['password'].encode ('utf-8')
        remember = False

        if 'remember' in params:
            remember = True

        # user = db.session.query(User).filter(User.username==username).first()
        user = User.query.filter_by (username=username)
        user = user.first ()

        if user:
            if user.is_password_correct (password):

                login_user (user)
                user.authenticated = True
                user.is_anonymous ()
                #
                flask.flash ('Logged in successfully.')

                next = flask.request.args.get ('next')
                # t=[]
                t = [user.username]
                global userdatastore
                userdatastore = t
                global userisauth
                userisauth = True
                # is_safe_url should check if the url is safe for redirects.
                # See http://flask.pocoo.org/snippets/62/ for an example.


                return flask.redirect (next or flask.url_for ('dashboard'))
            else:
                return flask.render_template ('public/signin.html')
        else:
            return flask.render_template ('public/signin.html')


@app.route ('/signup', methods=['POST', 'GET'])
def index2():
    if request.method == 'GET':
        return render_template ('public/signup.html')

    if request.method == 'POST':
        # login_manager.login_view = '/signup'

        params = request.form
        username = params['username']
        password = params['password']
        email = params['email']
        text1 = params['username']
        user = db.session.query (User).filter (User.username == username).first ()
        emailusr = db.session.query (User).filter (User.email == email).first ()
        print (user)
        if user:
            return render_template ('public/signup.html')

        if emailusr:
            return render_template ('public/signup.html')

        else:
            try:
                password = bcrypt.generate_password_hash (password)
                # print password
                user = User ()
                user.username = username
                user._password = password
                user.email = email

                db.session.add (user)

                db.session.commit ()

                text = text1 + make_footer (username, password, email)
                send_mail (username, text)

                print (user._password)
                print (user.email)
                return render_template ('public/signin.html')

            except:
                return render_template ('public/signup.html')


@app.route ('/trynow')
def trynow():
    if request.method == 'GET':
        return render_template ('public/trynow.html')
        #


@app.route ("/logout")
@login_required
def logout():
    logout_user ()
    return redirect (somewhere)





@app.route ('/Usernamechanged', methods=['POST', 'GET'])
def paymentpaypalonetime():
    if request.method == 'GET':
        payment_id = request.args.get ('paymentId', None)
        payer_id = request.args.get ('PayerID', None)
        # payer_id = request.args.get('PayerID', None)
        payment = paypalrestsdk.Payment.find(payment_id)
        # billing_agreement_response = BillingAgreement.execute (payment_token)
        # print("BillingAgreement[%s] executed successfully" % billing_agreement_response.id)

        # # print payer_id
        # # print payment_id

        if payment.execute({"payer_id": payer_id}):
            payment = paypalrestsdk.Payment.find(payment_id)

            payment_history = paypalrestsdk.Payment.all({"count": 1})
            r = payment_history.payments
            for i in r:
                # print i['first_name']
                # print i['last_name']
                # print i['int r[0]email']


                status=i['state']
                # print i['create_time']
                if (status == 'approved'):
                    userpy = Userpayment()
                    userpy.username = status
                    userpy.package1 = status
                    userpy.package2 = '0'
                    userpy.email = status
                    userpy.status = status
                    # print  userpy.username
                    db.session.add(userpy)
                    db.session.commit()
                    # print "payemt done"
                    return render_template('public/test1%23#/.html', i=i)
                else:
                    return render_template('admin_boostlikes/index.html')

        # else:
        #     return render_template('admin_boostlikes/index.html')




@app.route ('/changeUser', methods=['POST', 'GET'])
def paymentpaypalcancel():
    if request.method == 'POST':
        payment = paypalrestsdk.Payment ({
            "intent": "sale",

            # Payer
            # A resource representing a Payer that funds a payment
            # Payment Method as 'paypal'
            "payer": {
                "payment_method": "paypal"},

            # Redirect URLs
            "redirect_urls": {
                "return_url": "http://0.0.0.0:2300/Usernamechanged",
                "cancel_url": "http://localhost:3000/"},

            # Transaction
            # A transaction defines the contract of a
            # payment - what is the payment for and who
            # is fulfilling it.
            "transactions": [{

                # ItemList
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": "0.01",
                        "currency": "CAD",
                        "quantity": 1}]},

                # Amount
                # Let's you specify a payment amount.
                "amount": {
                    "total": "0.01",
                    "currency": "CAD"},
                "description": "This is the payment transaction description."}]})

        # Create Payment and return status
        if payment.create():
            print("Payment[%s] created successfully" % (payment.id))
            # Redirect the user to given approval url
            for link in payment.links:
                if link.rel == "approval_url":
                    # Convert to str to avoid google appengine unicode issue
                    # https://github.com/paypal/rest-api-sdk-python/pull/58
                    approval_url = str (link.href)

                    print("Redirect for approval: %s" % (approval_url))

                    return approval_url

        else:
            print("Error while creating payment:")
            print(payment.error)
        # print request.data
        # print request.json
        # return 'to get '


@app.route ('/userauth', methods=['GET'])
def userauth():
    if request.method == 'GET':
        # username = request.get_json()

        us = userdatastore
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


@app.route ('/change_accountname', methods=['POST'])
def payementsuccess():
    if request.method == 'GET':
        return render_template ('admin_boostlikes/index.html')

    if request.method == 'POST':
        return True
        # payment = Payment ({
        #     "intent": "sale",
        #
        #     # Payer
        #     # A resource representing a Payer that funds a payment
        #     # Payment Method as 'paypal'
        #     "payer": {
        #         "payment_method": "paypal"},
        #
        #     # Redirect URLs
        #     "redirect_urls": {
        #         "return_url": "http://0.0.0.0:2300/",
        #         "cancel_url": "http://localhost:3000/"},
        #
        #     # Transaction
        #     # A transaction defines the contract of a
        #     # payment - what is the payment for and who
        #     # is fulfilling it.
        #     "transactions": [{
        #
        #         # ItemList
        #         "item_list": {
        #             "items": [{ss
        #                 "name": "item",
        #                 "sku": "item",
        #                 "price": "0.01",
        #                 "currency": "CAD",
        #                 "quantity": 1}]},
        #
        #         # Amount
        #         # Let's you specify a payment amount.
        #         "amount": {
        #             "total": "0.01",
        #             "currency": "CAD"},
        #         "description": "This is the payment transaction description."}]})

        # Create Payment and return status
        # if payment.create ():
        #     print("Payment[%s] created successfully" % (payment.id))
        #     # Redirect the user to given approval url
        #     for link in payment.links:
        #         if link.rel == "approval_url":
        #             # Convert to str to avoid google appengine unicode issue
        #             # https://github.com/paypal/rest-api-sdk-python/pull/58
        #             approval_url = str (link.href)
        #             return approval_url
        #             print("Redirect for approval: %s" % (approval_url))
        # else:
        #     print("Error while creating payment:")
        #     print(payment.error)
        # # params = request.form
        # # status = request.gets_json()
        # status = request.json['s']
        # package1 = request.json['s']
        # # print status
        # # return render_template('admin_boostlikes/autoround.html')
        #
        #
        # if (status == 'approved'):
        #     userpy = Userpayment ()
        #     userpy.username = status
        #     userpy.package1 = package1
        #     userpy.package2 = '0'
        #     userpy.email = status
        #     userpy.status = status
        #     # print  userpy.username
        #     db.session.add (userpy)
        #     db.session.commit ()
        #     # print "payemt done"
        #     return render_template ('admin_boostlikes/autoround.html')
        # else:
        #     return render_template ('admin_boostlikes/index.html')











@app.route ('/home#', methods=['GET', 'POST'])
# @cross_origin()
# @auth.verify_password
@login_required

def dashboard():
    if request.method == 'GET':
        print   userdatastore

        return render_template ('public/test1.html')
    else:
        return render_template ('public/signin.html')



@app.route ('/start_paypal', methods=['POST'])
# @cross_origin()
# @auth.verify_password
# @login_required
def startpaypal():
    if request.method == 'POST':

        username  = request.json['username']

        billing_plan = BillingPlan ({
            "name": "navjotbabrah",
            "description": "Create Plan for Regular",
            "merchant_preferences": {
                "auto_bill_amount": "yes",
                "cancel_url": "http://pythonapps.com:2300/home%23#/Autoround?failed",
                "initial_fail_amount_action": "continue",
                "max_fail_attempts": "0",
                "return_url": "http://pythonapps.com:2300/home%23#/Autoround?success"

            },
            "payment_definitions": [
                {
                    "amount": {
                        "currency": "CAD",
                        "value": "0.01"
                    },


                    "cycles": "0",
                    "frequency": "MONTH",
                    "frequency_interval": "1",
                    "name": "Regular 1",
                    "type": "REGULAR"
                }
            ],
            "type": "INFINITE"
        })
        import datetime
        start_date =(datetime.datetime.utcnow()+ datetime.timedelta(minutes=3)).strftime('%Y-%m-%dT%H:%M:%SZ')
        print start_date
        if billing_plan.create ():
            print("Billing Plan [%s] created successfully" % billing_plan.id)
            global billing_id

            # billing_id = billing_plan.id
            # Activate billing plan
            if billing_plan.activate ():
                billing_plan = BillingPlan.find (billing_plan.id)
                # print  (billing_plan.to_dict())
                print("Billing Plan [%s] state changed to %s" % (billing_plan.id, billing_plan.state))
                print billing_plan
                billing_agreement = BillingAgreement ({
                    "name": "dj",
                    "description": "Agreement for organization plan",
                    "start_date":start_date,
                    "plan": {
                        "id": billing_plan.id
                    },
                    "payer": {
                        "payment_method": "paypal"
                    },
                    "shipping_address": {
                        "line1": "StayBr111idge Suites",
                        "line2": "Cro12ok Street",
                        "city": "San Jose",
                        "state": "CA",
                        "postal_code": "95112",
                        "country_code": "US"
                    }
                })

                # logging.basicConfig (level=logging.INFO)


                if billing_agreement.create():
                    # Extract redirect url
                    for link in billing_agreement.links:
                        if link.method == "REDIRECT":
                            # Capture redirect url
                            redirect_url = str (link.href)
                            print redirect_url
                            return redirect_url

                            # REDIRECT USER TO redirect_url
                else:
                    print(billing_agreement.error)

                    # if billing_agreement.create():
                #     print("Billing Agreement created successfully")
                #     for link in billing_agreement.links:
                #         if link.rel == "approval_url":
                #             approval_url = link.href
                #             # paypal process
                #             print approval_url
                #             return redirect(url_for (approval_url))
                #
                #             # return flask.render_template('public/home.html')

            else:
                print(billing_plan.error)
        else:
            print(billing_plan.error)


@app.route ("/subscribe", methods=['POST', 'GET'])
def subscribe():
    if request.method == 'POST':
        payment_token=request.json['token']
        o=request.args.get('paymentId')
        global userdatastore
        print userdatastore
        userdatastore = 'dj'
        print userdatastore
        # payment_id = billing_id


        billing_agreement_response  = BillingAgreement.execute(payment_token)
        print billing_agreement_response
        start_date, end_date = "2017-07-03", "2017-07-20"

        billing_agreement = BillingAgreement.find (billing_agreement_response.id)
        # print billing_agreement.final_payment_date
        # transactions = billing_agreement.search_transactions(start_date, end_date)
        # print transactions
        print("Got Billing Agreement Details for Billing Agreement[%s]" % (billing_agreement.id))



        # bill_id = billing_agreement_response.id
        # billing_agreement =  BillingAgreement.find(bill_id)
        # planstart_date= billing_agreement_response.start_date
        # print planstart_date

        # payment = paypalrestsdk.Payment.find(billing_agreement.id)

        # print payment
        # Get List of Payments
        # payment_history = paypalrestsdk.Payment.all ({"count": 1})
        # print payment_history

        # Get List of Payments

        # print billing_agreement

        userpy = userpackage()
        userpy.username = userdatastore
        userpy.Auto_ac_name = 'new'
        userpy.email = 'nav'
        userpy.Listlikepackage = 'nav'
        userpy.usr_email = "asdsad"

        # print  userpy.username
        db.session.add (userpy)
        db.session.commit()

        # print("BillingAgreement[%s] executed successfully" % billing_agreement_response.id)

        return 'sussesc'


def send_mail(text, resume=None):
    if resume:
        files = [('attachment', resume)]

    else:
        files = []
    return requests.post (URL,
                          auth=("api", MAILGUN_API_KEY),
                          files=files,
                          data={"from": "Boostuplikes <postmaster@sandbox047085ca4cac4999b35d70a3e5be1c30.mailgun.org>",
                                "to": ['navjotbabrah27@gmail.com'],
                                "subject": 'Boostuplikes',
                                "text": text
                                })


def make_footer(username, password, email):
    t = '\n\nRegards,\n'
    t += username + '\n'
    t += password + '\n'
    # t += email + '\n'
    # t += url  + '\n'


    return t


    # return 'http://0.0.0.0:2300/'


if __name__ == '__main__':
    app.run (host='0.0.0.0',port=23000)

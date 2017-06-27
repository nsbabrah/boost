# import SQLAlchemy as SQLAlchemy
from flask import Flask, render_template, request
import requests
from flask.ext.sqlalchemy import SQLAlchemy

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
from flask_cors import CORS, cross_origin
import paypalrestsdk
import flask_login
from flask_login import LoginManager, login_user
# cors = CORS(app, resources={r"/test/*": {"origins": "*"}})

from OpenSSL import SSL
import models
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

# login_manager = LoginManager()
app = Flask(__name__, static_folder='static', static_url_path='/static')
# login_manager.init_app(app)
# CORS(app)
# logging.getLogger('flask_cors').level = logging.DEBUG
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('flask_cors').level = logging.DEBUG
my_api = paypalrestsdk.configure({
    "mode": "live",  # sandbox or live
    "client_id": "ARfJ7TKcE2_LI3EnqpX9gfAu5q0N_5AIetmWIvLdwQdRkSDP5nXxjLiXJsgQzuT5yLdwUbJ_WX8vNzNN",
    "client_secret": "EDnnJIy3J41BACVB69NxZMf01sZiU0UEM31NdE9GkpGdj4Da8XbFdqwTESYrNZmevI8Uuwg6EP-s4SlR"})

my_api.get_access_token()


from config import *
from model import *
# from paymnts import *
app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SECRET_KEY'] = '769876tr8629r9yog^%&^*13*^&)&*^%&()'
# the payment transaction description."}]})

# login_manager.login_view = '/signin'
# from controllers import *
# DB instance init
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#
# def commit(obj):
#     if type(obj) == list:
#         for i in obj:
#             db.session.add(i)
#         db.session.commit()
#     else:
#         db.session.add(obj)
#         db.session.commit()
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     '''User Loader for flask-login
#     :params
#      user_id -> email
#     '''
#     return User.query.get(user_id)




@app.route('/')
def index():

    return render_template('public/index.html')


@app.route('/signin', methods=['POST', 'GET'])

def index1():
    if request.method == 'GET':
        # logout_user(user)

        return render_template('public/signin.html')

    if request.method == 'POST':


        params = request.form
        username = params['username']
        password = params['password'].encode('utf-8')

        # user= db.session.query(db.exists().where(User.username ==  username)).scalar()
        # print user.password
        user = db.session.query(User).filter(User.username==username).first()
        print user.username

        # print user
        # if 'remember' in params:
        #     remember = True

        # user = User(username,password,email)
        # print  user._password

        # user =db.session.query(User).filter(User.username==username, User._password==password)
        #
        # user = user.one()
        # print user
        # print user.username
        # user = User (username,password)
        # user = db.session.query(User.id).filter(User.username==username,User._password==password).first()

        #
        import bcrypt
        # password = bcrypt.generate_password_hash(password)
        print password
        if user:
            # print user._password
            if user.is_password_correct(password):
                return redirect (url_for ('test'))
            else:
                return render_template('public/signin.html', fail=True)

            # print db.session.query(user)
            # # print dir(user)
            # user =User(username,password)

            # print (user._password)
            # if user._password):
            #     login_user (user)
            #     user.authenticated = True
            #     db.session.add (user)
            #     db.session.commit ()


            # return redirect (url_for ('test'))
            #  print (user.username)
            # # #  user.authenticated = False
            # print user.verify_password(password)
            # pwhash = bcrypt.check_password_hash(password,user

            # p = bcrypt.check_password_hash(password,user._password)
            # print p
            # if user._password == p:
            #      # print (user.password)
            #      return render_template ('public/text.html')
            #


            #      # print user.username
            #     #  login_user(user)



        else:
            return render_template('public/signin.html', fail=True)

            # print 'asasas'
            # return render_template('public/trynow.html')

        #     if user.is_password_correct(password):
        #         # login_user(user)
        #         # user.authenticated = True
        #         # db.session.add(user)
        #         # db.session.commit()
        #         return render_template('public/test.html')
        #
        # return render_template('public/signin.html', fail=True)
        #



@app.route('/signup', methods=['POST', 'GET'])
def index2():

    if request.method == 'GET':
        return render_template('public/signup.html')

    if request.method == 'POST':
        # login_manager.login_view = '/signup'

        params = request.form
        username = params['username']
        password = params['password']
        email = params['email']
        text1 = params['username']
        password = bcrypt.generate_password_hash(password)
        print password
        user = User()
        user.username=username
        user._password=password
        user.email=email

        db.session.add(user)

        db.session.commit()

        text =  text1  + make_footer(username,password,email)
        send_mail(username,text)
        # login_user(user)
        # user.authenticated = True

        return render_template('public/signin.html')
        # return render_template('public/trynow.html')





@app.route('/trynow')
def trynow():
    if request.method == 'GET':
        return render_template('public/trynow.html')
        #


@app.route('/home')
def indexhome():
    if request.method == 'GET':
        return render_template('adminm/home.html')


@app.route('/test')
def test():
    if request.method == 'GET':
        return render_template('public/test.html')
        #      #


@app.route('/about')
def indexabout():
    if request.method == 'GET':
        return render_template('public/about.html')


@app.route('/Boost')
def index3():
    if request.method == 'GET':
        return render_template('admin_boostlikes/Boost.html')


@app.route('/Listlike')
def index4():
    if request.method == 'GET':
        return render_template('admin_boostlikes/Listlike.html')
        #


@app.route('/Payementsuccessful', methods=['POST', 'GET'])
def paymentpaypalonetime():
    if request.method == 'GET':

        payment_id = request.args.get('paymentId', None)
        payer_id = request.args.get('PayerID', None)
        # payer_id = request.args.get('PayerID', None)
        payment = paypalrestsdk.Payment.find(payment_id)

        # print payer_id
        # print payment_id

        if payment.execute({"payer_id": payer_id}):
            payment = paypalrestsdk.Payment.find(payment_id)

            # Get List of Payments
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
                    return render_template('public/test.html', i=i)
                else:
                    return render_template('admin_boostlikes/index.html')

        else:
            return render_template('admin_boostlikes/index.html')


@app.route('/Payementcancel', methods=['POST', 'GET'])
def paymentpaypalcancel():
    if request.method == 'GET':

            # pending_payment.state = payment.state
            # pending_payment.updated_at = datetime.strptime(payment.update_time, "%Y-%m-%dT%H:%M:%SZ")
        return render_template('admin_boostlikes/ERROR/payementcancel.html')


@app.route('/dashboard', methods=['GET'])
def index5():
    if request.method == 'GET':
        return render_template('admin_boostlikes/index.html')


@app.route('/payementpaypal', methods=['POST'])
def payementsuccess():
    if request.method == 'GET':
        return render_template('admin_boostlikes/index.html')

    if request.method == 'POST':
            # params = request.form
            # status = request.gets_json()
            status=request.json['s']
            package1=request.json['s']
            # print status
            # return render_template('admin_boostlikes/autoround.html')


            if(status == 'approved'):
               userpy = Userpayment()
               userpy.username = status
               userpy.package1 = package1
               userpy.package2 = '0'
               userpy.email=status
               userpy.status=status
               # print  userpy.username
               db.session.add(userpy)
               db.session.commit()
               # print "payemt done"
               return render_template('admin_boostlikes/autoround.html')
            else:
               return render_template('admin_boostlikes/index.html')



@app.route('/test', methods=['POST', 'GET'])
#@cross_origin()
# @login_required.user.id
def index6():

    if request.method == 'GET':

        return render_template('public/test.html')

    if request.method == 'POST':
        parms=request.data
        # print parms
        # # return parms
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://0.0.0.0:2300/Payementsuccessful",
                "cancel_url": "http://0.0.0.0:2300/Payementcancel"},

            "transactions": [{
                # "type": "SHIPPING",

                "amount": {
                    "total": "0.01",
                    "currency": "CAD"},
                # "type": "no_shipping"
                "description": "creating a payment"}]})
        # payment.create()


        if payment.create():
            print("Payment created successfully")
            for link in payment.links:
                if link.method == "REDIRECT":
                    redirect_url = str(link.href)

                    print('Redirect for approval: {}'.format(redirect_url))
                    url = ('{}'.format(redirect_url))
                    # return re('Redirect for approval: {}'.format(redirect_url))direct(redirect_urls)
                    # payer_id = request.args.get('payerId')
                    # payment_id = request.args.get('paymentId')
                    # token = request.args.get('token')
                    return url
                    # return render_template('admin_boostlikes/index.html')

        else:
            print(payment.error)
            return render_template('admin_boostlikes/autoround.html')

def send_mail(text,resume=None):



		if resume:
			files = [('attachment',resume)]

		else:
			files = []
		return requests.post(URL,
        auth = ("api", MAILGUN_API_KEY),
         files=files,
        data = {"from": "Boostuplikes <postmaster@sandbox047085ca4cac4999b35d70a3e5be1c30.mailgun.org>",
               "to": ['navjotbabrah27@gmail.com'],
               "subject": 'Boostuplikes',
               "text": text
               })


def make_footer(username,password,email):
	t = '\n\nRegards,\n'
	t += username+ '\n'
	t += password + '\n'
	t += email + '\n'
    # t += url  + '\n'


	return t


        # return 'http://0.0.0.0:2300/'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2300, debug=True, threaded=True)

from flask import Flask, render_template, request
import requests
from paypalrestsdk import Payment
import logging
import json
# import jsonify
from paypalrestsdk import BillingPlan, BillingAgreement
from flask_bcrypt import Bcrypt
# from init import botstart
from flask_cors import CORS, cross_origin
import paypalrestsdk
from flask_login import LoginManager, login_user

from OpenSSL import SSL
import models
# from boost.model import *
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
login_manager = LoginManager()
app = Flask(__name__, static_folder='static', static_url_path='/static')
login_manager.init_app(app)
# CORS(app)
# logging.getLogger('flask_cors').level = logging.DEBUG
logging.basicConfig(level=logging.INFO)
my_api = paypalrestsdk.configure({
    "mode": "live",  # sandbox or live
    "client_id": "ARfJ7TKcE2_LI3EnqpX9gfAu5q0N_5AIetmWIvLdwQdRkSDP5nXxjLiXJsgQzuT5yLdwUbJ_WX8vNzNN",
    "client_secret": "EDnnJIy3J41BACVB69NxZMf01sZiU0UEM31NdE9GkpGdj4Da8XbFdqwTESYrNZmevI8Uuwg6EP-s4SlR"})

my_api.get_access_token()

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://192.168.2.56:2300/Payementsuccessful",
        "cancel_url": "http://192.168.2.56:2300/Payementcancel"},

    "transactions": [{
        # "type": "SHIPPING",

        "amount": {
            "total": "0.01",
            "currency": "CAD"},
        # "type": "no_shipping"
        "description": "creating a payment"}]})

from config import *
from model import *
# from paymnts import *
app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SECRET_KEY'] = '769876tr8629r9yog^%&^*13*^&)&*^%&()'
# the payment transaction description."}]})

login_manager.login_view = '/signin'
# from controllers import *
# DB instance init
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(id):
    '''User Loader for flask-login
    :params
     user_id -> email
    '''
    user = model.User.query.get(id)
    if user:
        return user
    else:
        return None


def commit(obj):
    if type(obj) == list:
        for i in obj:
            model.db.session.add(i)
        model.db.session.commit()
    else:
        model.db.session.add(obj)
        model.db.session.commit()


@app.route('/')
def index():

    return model.render_template('public/index.html')


@app.route('/signin', methods=['POST', 'GET'])
def index1():
    if model.request.method == 'GET':
        return model.render_template('public/signin.html')

    if model.request.method == 'POST':

        params = model.request.form
        username = params['username']
        password = params['password']
        print password
        user = 'nav'
        user = model.User.query.filter_by(username=username)
        user = user.first()

        if 'remember' in params:
            remember = True

        if user:
            print 'asasas'
            # return render_template('public/trynow.html')

            if user.is_password_correct(password):
                login_user(user)
                user.authenticated = True
                # db.session.add(user)
                # db.session.commit()
                return model.render_template('admin_boostlikes/index.html')

        return model.render_template('public/signin.html', fail=True)


@app.route('/admin')
def admin():
    if model.request.method == 'GET':
        return model.render_template('admin_boostlikes/index.html')
        # admin
        # admin


@app.route('/signup', methods=['POST', 'GET'])
def index2():

    if model.request.method == 'GET':
        return model.render_template('public/signup.html')

    if model.request.method == 'POST':
        login_manager.login_view = '/signup'

        params = model.request.form
        username = params['username']
        password = params['password']
        email = params['email']
        user = model.User()
        user.username = username
        user.password = password
        user.email = email
        model.db.session.add(user)
        model.db.session.commit()
        return model.render_template('public/index.html')
        # return render_template('public/trynow.html')


@app.route('/trynow')
def trynow():
    if model.request.method == 'GET':
        return model.render_template('public/trynow.html')
        #


@app.route('/home')
def indexhome():
    if model.request.method == 'GET':
        return model.render_template('adminm/home.html')


@app.route('/test')
def test():
    if model.request.method == 'GET':
        return model.render_template('public/test.html')
        #      #


@app.route('/about')
def indexabout():
    if model.request.method == 'GET':
        return model.render_template('public/about.html')


@app.route('/Boost')
def index3():
    if model.request.method == 'GET':
        return model.render_template('admin_boostlikes/Boost.html')


@app.route('/Listlike')
def index4():
    if model.request.method == 'GET':
        return model.render_template('admin_boostlikes/Listlike.html')
        #


@app.route('/Payementsuccessful', methods=['POST', 'GET'])
def paymentpaypalonetime():
    if model.request.method == 'GET':

        payment_id = model.request.args.get('paymentId', None)
        payer_id = model.request.args.get('PayerID', None)
        # payer_id = request.args.get('PayerID', None)
        payment = paypalrestsdk.Payment.find(payment_id)

        print payer_id
        print payment_id

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
                print i['create_time']
                if (status == 'approved'):
                    userpy = Userpayment()
                    userpy.username = status
                    userpy.package1 = status
                    userpy.package2 = '0'
                    userpy.email = status
                    userpy.status = status
                    print  userpy.username
                    model.db.session.add(userpy)
                    model.db.session.commit()
                    print "payemt done"
                    return render_template('public/test.html', i=i)
                else:
                    return render_template('admin_boostlikes/index.html')

        else:
            return render_template('admin_boostlikes/index.html')


@app.route('/Payementcancel', methods=['POST', 'GET'])
def paymentpaypalcancel():
    if model.request.method == 'GET':

            # pending_payment.state = payment.state
            # pending_payment.updated_at = datetime.strptime(payment.update_time, "%Y-%m-%dT%H:%M:%SZ")
        return model.render_template('admin_boostlikes/ERROR/payementcancel.html')


@app.route('/dashboard', methods=['GET'])
def index5():
    if model.request.method == 'GET':
        return model.render_template('admin_boostlikes/index.html')


@app.route('/payementpaypal', methods=['POST'])
def payementsuccess():
    if model.request.method == 'GET':
        return model.render_template('admin_boostlikes/index.html')

    if model.request.method == 'POST':
            # params = request.form
            # status = request.gets_json()
            status=model.request.json['s']
            package1=model.request.json['s']
            print status
            # return render_template('admin_boostlikes/autoround.html')


            if(status == 'approved'):
               userpy = Userpayment()
               userpy.username = status
               userpy.package1 = package1
               userpy.package2 = '0'
               userpy.email=status
               userpy.status=status
               print  userpy.username
               model.db.session.add(userpy)
               model.db.session.commit()
               print "payemt done"
               return model.render_template('admin_boostlikes/autoround.html')
            else:
               return model.render_template('admin_boostlikes/index.html')



@app.route('/AutoRound', methods=['POST', 'GET'])
# @cross_origin(origin='*')
def index6():

    if model.request.method == 'GET':

        return model.render_template('admin_boostlikes/autoround.html')

    if model.request.method == 'POST':

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
                    return model.redirect(url)

        else:
            print(payment.error)
            return model.render_template('admin_boostlikes/autoround.html')


            return model.render_template('admin_boostlikes/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2300, debug=True, threaded=True)

from flask import Flask, render_template, request
import requests
from paypalrestsdk import Payment
import logging
# import jsonify
from paypalrestsdk import BillingPlan, BillingAgreement
from flask.ext.bcrypt import Bcrypt
# from init import botstart
from flask_cors import CORS, cross_origin
import paypalrestsdk
from flask_login import LoginManager,login_user
# from controllers import *
from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('yourserver.key')
# context.use_certificate_file('yourserver.crt')
login_manager = LoginManager()
app = Flask(__name__, static_folder='static', static_url_path='/static')
login_manager.init_app(app)
# CORS(app)
# logging.getLogger('flask_cors').level = logging.DEBUG
logging.basicConfig(level=logging.INFO)
my_api=paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "ARfJ7TKcE2_LI3EnqpX9gfAu5q0N_5AIetmWIvLdwQdRkSDP5nXxjLiXJsgQzuT5yLdwUbJ_WX8vNzNN",
  "client_secret": "EDnnJIy3J41BACVB69NxZMf01sZiU0UEM31NdE9GkpGdj4Da8XbFdqwTESYrNZmevI8Uuwg6EP-s4SlR" })

my_api.get_access_token()

payment = paypalrestsdk.Payment({
"intent": "sale",
"payer": {
"payment_method": "paypal" },
"redirect_urls": {
"return_url": "http://192.168.2.56:3000/dashboard",
"cancel_url": "http://192.168.2.56:3000/" },

"transactions": [ {
"amount": {
"total": "0.01",
"currency": "CAD" },
"description": "creating a payment" } ] })
# payment = paypalrestsdk.Payment(payment)

# api=paypalrestsdk.configure({
#   'mode': 'sandbox',
#   'client_id': 'AYIV-LTwqnn52pR-g-OHDhEp36DD3aw5PiKP866R3MVePcNg0NTSRgAUAbiUrZsyaJHv5o_L9fSOF3aA',
#   'client_secret': 'gmLaDAgbQXYnSLh7vw5Hfg9Fo4vBSY-WwKAroE3fp2sEbP'
# })

# payment = paypalrestsdk.Payment({
# "intent": "sale",
# "payer": {
# "payment_method": "paypal" },
# "redirect_urls": {
# "return_url": "http://127.0.0.1:8023/AutoRound",
# "cancel_url": "http://127.0.0.1:8023/AutoRound" },
#
# "transactions": [ {
# "amount": {
# "total": "12",
# "currency": "USD" },
# "description": "creating a payment" } ] } )
#
#
# payment.create()

# verify='../../etc/ssl/certs/cacert.org.pem'
# response = requests.get('https://lists.cacert.org', verify=verify)
# Bcrypt Config
from config import *
from models import *
app.config['SQLALCHEMY_DATABASE_URI'] = DB
app.config['SECRET_KEY'] = '769876tr8629r9yog^%&^*)&*^%&()'
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
    user = User.query.get(id)
    if user:
        return user
    else:
        return None
def commit(obj):
	if type(obj) == list:
		for i in obj:
			db.session.add(i)
		db.session.commit()
	else:
		db.session.add(obj)
		db.session.commit()


@app.route('/')
def index():
    #
    # page = requests.get("http://google.com")
    # page.status_code
    # soup = BeautifulSoup(page.content, 'html.parser')
    # soup.find_all(id="lga")

    return render_template('public/index.html')


@app.route('/signin', methods=['POST', 'GET'])
def index1():
    if request.method == 'GET':
        return render_template('public/signin.html')

    if request.method == 'POST':

        params = request.form
        username = params['username']
        password = params['password']
        print password
        user = 'nav'
        user = User.query.filter_by(username=username)
        user = user.first()
                # password = User.query.filter_by(password=password)
        # # user = user.first()
        # registered_user = User.query.filter_by(username=username,password=password).first()
        # if registered_user is None:
        #     flash('Username or Password is invalid' , 'error')
        # return redirect(url_for('login'))
        # login_user(registered_user)
        # flash('Logged in successfully')
        # return redirect(request.args.get('next') or url_for('index'))
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
                return render_template('admin_boostlikes/index.html')


        return render_template('public/signin.html',fail=True)



@app.route('/admin')
def admin():
    if request.method == 'GET':
        return render_template('admin_boostlikes/index.html')
        # admin
        # admin


@app.route('/signup', methods=['POST','GET'])
def index2():

    if request.method == 'GET':
        return render_template('public/signup.html')


    if request.method == 'POST':
        login_manager.login_view = '/signup'

        params = request.form
        username = params['username']
        password = params['password']
        email = params['email']
        user = User()
        user.username = username
        user.password = password
        user.email = email
        db.session.add(user)
        db.session.commit()
        return render_template('public/index.html')
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
        #


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


@app.route('/dashboard',methods=['GET'])
def index5():
    if request.method == 'GET':
        # payer_id = request.args.get('payerId')
        # # payer_id = request.args.get('payerId')
        # payment_id = request.args.get('paymentId')
        # # token = request.args.get('token')
        # # state=request.args.get('state')
        # payment_token = request.args.get('token', '')
        # billing_agreement_response = BillingAgreement.execute(str(request.args.get('payerId')))
        # return redirect(url_for('/AutoRound'))
        payment_id = request.args.get('paymentId', None)
        payer_id = request.args.get('PayerID', None)
        payment = paypalrestsdk.Payment.find(payment_id)
        # pending_payment = PayPalPayment.query.filter_by(token=token).filter_by(state='created').first_or_404()
        #
        # try:
        #     payment = paypalrestsdk.Payment.find(pending_payment.payment_id)
        # except paypalrestsdk.exceptions.ResourceNotFound as ex:
        #     print('Paypal resource not found: {}'.format(ex))
        #     abort(404)

        if payment.execute({"payer_id": payer_id}):
            # pending_payment.state = payment.state
            # pending_payment.updated_at = datetime.strptime(payment.update_time, "%Y-%m-%dT%H:%M:%SZ")
            return render_template('admin_boostlikes/autoround.html')
        else:
            return render_template('admin_boostlikes/index.html')

            # db.session.commit()

        # print payment_id
        # print payer_id
        # payment = paypalrestsdk.Payment.find(payment_id)
        #
        # if payment.execute({"payer_id": 'DUFRQ8GWYMJXC'}):
        #   print("Payment execute successfully")
        #   return render_template('admin_boostlikes/index.html')
        #   #
        # else:
        #   print(payment.error) # Error Hash
        #   return render_template('admin_boostlikes/autoround.html')



@app.route('/AutoRound', methods=['POST', 'GET'])
# @cross_origin(origin='*')
def index6():

    if request.method == 'GET':
        #    payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")
           #
        #     # Get List of Payments
        #    payment_history = paypalrestsdk.Payment.all({"count": 10})
        #    payment_history.payments


           return render_template('admin_boostlikes/autoround.html')
            # Error Hash
                        #  response.headers.add('Access-Control-Allow-Origin', '*')




    if request.method == 'POST':

        if payment.create():
           print("Payment created successfully")
           for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                # response.headers.add('Access-Control-Allow-Origin', '*')
                print('Redirect for approval: {}'.format(redirect_url))
                url=('{}'.format(redirect_url))
                # return re('Redirect for approval: {}'.format(redirect_url))direct(redirect_urls)
                # payer_id = request.args.get('payerId')
                # payment_id = request.args.get('paymentId')
                # token = request.args.get('token')
                return redirect(url)


                # pending_payment = PayPalPayment.query.filter_by(token=token).filter_by(state='created').first_or_404()
                #
                # try:
                #     payment = paypalrestsdk.Payment.find(pending_payment.payment_id)
                # except paypalrestsdk.exceptions.ResourceNotFound as ex:
                #     print('Paypal resource not found: {}'.format(ex))
                #     abort(404)
                #     if payment.execute({"payer_id": payer_id}):
                #         pending_payment.state = payment.state
                #         pending_payment.updated_at = datetime.strptime(payment.update_time, "%Y-%m-%dT%H:%M:%SZ")
                #         db.session.commit()




        else:
           print(payment.error)
           return render_template('admin_boostlikes/autoround.html')

        # paypalrestsdk.configure({
        #   'mode': 'sandbox',
        #   'client_id': 'AYIV-LTwqnn52pR-g-OHDhEp36DD3aw5PiKP866R3MVePcNg0NTSRgAUAbiUrZsyaJHv5o_L9fSOF3aA',
        #   'client_secret': 'gmLaDAgbQXYnSLh7vw5Hfg9Fo4vBSY-WwKAroE3fp2sEbP'
        # })

        #    payment = paypalrestsdk.Payment.find("id")

        #    payment_history.payments
        #    print payment
        #    print(payment)
           return render_template('admin_boostlikes/index.html')






    #     return redirect(url_for('/AutoRound'))
    # else:
    #     return redirect(url_for('/'))
        # payment = paypalrestsdk.Payment({
        #           "intent": "sale",
        #           "payer": {
        #           "payment_method": "paypal" },
        #           "redirect_urls": {
        #           "return_url": "https://127.0.0.1:8023/AutoRound/",
        #           "cancel_url": "https://yoursite.com/canceled/" }, },api=api )
        #
        #
        #
        # # payment = paypalrestsdk.Payment(payment)
        # if payment.create():
        #     print("Payment[%s] created successfully" % (payment.id))
        #     for link in payment.links:
        #         if link.method == "REDIRECT":
        #             redirect_url = str(link.href)
        #             print('Redirect for approval: {}'.format(redirect_url))
        #             return redirect(redirect_urls)

# @app.route('/AutoRound', methods=['POST', 'GET'])
# def indexendpoint():
#
#     if request.method == 'GET':
#         payment = paypalrestsdk.Payment.find("Payment-ID")
#         payment.execute({"payer_id": "Payer-ID "})
#         return render_template('admin_boostlikes/index.html')
#

@app.route('/execute/', methods=['GET'])
def payment_paypal_execute():
    payment_id = request.GET.get('paymentId', None) or request.POST.get('paymentId', None)
    payer_id = request.GET.get('PayerID', None) or request.POST.get('PayerID', None)
    payment = paypalrestsdk.Payment.find(payment_id)
    pending_payment = PayPalPayment.query.filter_by(token=token).filter_by(state='created').first_or_404()

    try:
        payment = paypalrestsdk.Payment.find(pending_payment.payment_id)
    except paypalrestsdk.exceptions.ResourceNotFound as ex:
        print('Paypal resource not found: {}'.format(ex))
        abort(404)

    if payment.execute({"payer_id": payer_id}):
        pending_payment.state = payment.state
        pending_payment.updated_at = datetime.strptime(payment.update_time, "%Y-%m-%dT%H:%M:%SZ")
        db.session.commit()
        return render_template('payment/success.html', payment_id=payment.id, state=payment.state)

    return render_template('payment/error.html', payment_error=payment.error, step='Finallizing payment')
    # Redirect the user to given approval url


           #  engine.index6()
        # return render_template('admin_boostlikes/autoround.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, threaded=True)

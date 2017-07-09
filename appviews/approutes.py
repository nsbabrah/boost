from flask import Blueprint
# from flask import  render_template, g
# from flask_login import LoginManager, login_user, logout_user
from flask_login import logout_user, login_required, UserMixin
import flask_login
from controller import controller
from controller.controller import gen

from flask import render_template, request
print controller.gen()
# login_manager.session_protection = "strong"
from config import *


my_view = Blueprint('my_view', __name__)


userdatastore = None
userisauth = None
billing_id = None


@my_view.route ('/', methods=['POST', 'GET'])
def dashmain():
    if request.method == 'GET':
        return render_template('public/index.html')
        # logout_user(user)


#
# @my_view.route ('/trynow')
# def trynow():
#     if request.method == 'GET':
#         return render_template ('public/trynow.html')
#         #
#
#
# @app.route ("/logout")
# @login_required
# def logout():
#     logout_user ()
#     return redirect (somewhere)
#
#
#
#
#
# @app.route ('/Usernamechanged', methods=['POST', 'GET'])
# def paymentpaypalonetime():
#     if request.method == 'GET':
#         payment_id = request.args.get ('paymentId', None)
#         payer_id = request.args.get ('PayerID', None)
#         # payer_id = request.args.get('PayerID', None)
#         payment = paypalrestsdk.Payment.find(payment_id)
#         # billing_agreement_response = BillingAgreement.execute (payment_token)
#         # print("BillingAgreement[%s] executed successfully" % billing_agreement_response.id)
#
#         # # print payer_id
#         # # print payment_id
#
#         if payment.execute({"payer_id": payer_id}):
#             payment = paypalrestsdk.Payment.find(payment_id)
#
#             payment_history = paypalrestsdk.Payment.all({"count": 1})
#             r = payment_history.payments
#             for i in r:
#                 # print i['first_name']
#                 # print i['last_name']
#                 # print i['int r[0]email']
#
#
#                 status=i['state']
#                 # print i['create_time']
#                 if (status == 'approved'):
#                     userpy = Userpayment()
#                     userpy.username = status
#                     userpy.package1 = status
#                     userpy.package2 = '0'
#                     userpy.email = status
#                     userpy.status = status
#                     # print  userpy.username
#                     db.session.add(userpy)
#                     db.session.commit()
#                     # print "payemt done"
#                     return render_template('public/test1%23#/.html', i=i)
#                 else:
#                     return render_template('admin_boostlikes/index.html')
#
#         # else:
#         #     return render_template('admin_boostlikes/index.html')
#
#
#
#
# @app.route ('/changeUser', methods=['POST', 'GET'])
# def paymentpaypalcancel():
#     if request.method == 'POST':
#         payment = paypalrestsdk.Payment ({
#             "intent": "sale",
#
#             # Payer
#             # A resource representing a Payer that funds a payment
#             # Payment Method as 'paypal'
#             "payer": {
#                 "payment_method": "paypal"},
#
#             # Redirect URLs
#             "redirect_urls": {
#                 "return_url": "http://0.0.0.0:2300/Usernamechanged",
#                 "cancel_url": "http://localhost:3000/"},
#
#             # Transaction
#             # A transaction defines the contract of a
#             # payment - what is the payment for and who
#             # is fulfilling it.
#             "transactions": [{
#
#                 # ItemList
#                 "item_list": {
#                     "items": [{
#                         "name": "item",
#                         "sku": "item",
#                         "price": "0.01",
#                         "currency": "CAD",
#                         "quantity": 1}]},
#
#                 # Amount
#                 # Let's you specify a payment amount.
#                 "amount": {
#                     "total": "0.01",
#                     "currency": "CAD"},
#                 "description": "This is the payment transaction description."}]})
#
#         # Create Payment and return status
#         if payment.create():
#             print("Payment[%s] created successfully" % (payment.id))
#             # Redirect the user to given approval url
#             for link in payment.links:
#                 if link.rel == "approval_url":
#                     # Convert to str to avoid google appengine unicode issue
#                     # https://github.com/paypal/rest-api-sdk-python/pull/58
#                     approval_url = str (link.href)
#
#                     print("Redirect for approval: %s" % (approval_url))
#
#                     return approval_url
#
#         else:
#             print("Error while creating payment:")
#             print(payment.error)
#         # print request.data
#         # print request.json
#         # return 'to get '
#
#
# @app.route ('/userauth', methods=['GET'])
# def userauth():
#     if request.method == 'GET':
#         # username = request.get_json()
#
#         us = userdatastore
#         # if userisauth and userdatastore is not None:
#         user = db.session.query (userpackage.username, userpackage.Auto_ac_name, userpackage.Listlikepackage,
#                                  userpackage.usr_id).filter (userpackage.username == us).all ()
#
#         t = []
#         col = ["username", "Auto_ac_name", "listlike", "usr_id"]
#
#         for i in user:
#             t.append (list (i))
#
#         temp = []
#         for i in t:
#             temp.append (dict (zip (col, i)))
#         print (temp)
#         return json.dumps (temp)
#     else:
#         return {'auth': "false"}
#
#
# @app.route ('/change_accountname', methods=['POST'])
# def payementsuccess():
#     if request.method == 'GET':
#         return render_template ('admin_boostlikes/index.html')
#
#     if request.method == 'POST':
#         return True
#         # payment = Payment ({
#         #     "intent": "sale",
#         #
#         #     # Payer
#         #     # A resource representing a Payer that funds a payment
#         #     # Payment Method as 'paypal'
#         #     "payer": {
#         #         "payment_method": "paypal"},
#         #
#         #     # Redirect URLs
#         #     "redirect_urls": {
#         #         "return_url": "http://0.0.0.0:2300/",
#         #         "cancel_url": "http://localhost:3000/"},
#         #
#         #     # Transaction
#         #     # A transaction defines the contract of a
#         #     # payment - what is the payment for and who
#         #     # is fulfilling it.
#         #     "transactions": [{
#         #
#         #         # ItemList
#         #         "item_list": {
#         #             "items": [{ss
#         #                 "name": "item",
#         #                 "sku": "item",
#         #                 "price": "0.01",
#         #                 "currency": "CAD",
#         #                 "quantity": 1}]},
#         #
#         #         # Amount
#         #         # Let's you specify a payment amount.
#         #         "amount": {
#         #             "total": "0.01",
#         #             "currency": "CAD"},
#         #         "description": "This is the payment transaction description."}]})
#
#         # Create Payment and return status
#         # if payment.create ():
#         #     print("Payment[%s] created successfully" % (payment.id))
#         #     # Redirect the user to given approval url
#         #     for link in payment.links:
#         #         if link.rel == "approval_url":
#         #             # Convert to str to avoid google appengine unicode issue
#         #             # https://github.com/paypal/rest-api-sdk-python/pull/58
#         #             approval_url = str (link.href)
#         #             return approval_url
#         #             print("Redirect for approval: %s" % (approval_url))
#         # else:
#         #     print("Error while creating payment:")
#         #     print(payment.error)
#         # # params = request.form
#         # # status = request.gets_json()
#         # status = request.json['s']
#         # package1 = request.json['s']
#         # # print status
#         # # return render_template('admin_boostlikes/autoround.html')
#         #
#         #
#         # if (status == 'approved'):
#         #     userpy = Userpayment ()
#         #     userpy.username = status
#         #     userpy.package1 = package1
#         #     userpy.package2 = '0'
#         #     userpy.email = status
#         #     userpy.status = status
#         #     # print  userpy.username
#         #     db.session.add (userpy)
#         #     db.session.commit ()
#         #     # print "payemt done"
#         #     return render_template ('admin_boostlikes/autoround.html')
#         # else:
#         #     return render_template ('admin_boostlikes/index.html')
#
#
#
#
#
#
#
#
#


@my_view.route ('/home#', methods=['GET', 'POST'])
# @cross_origin()
# @auth.verify_password
@login_required

def dashboard():
    if request.method == 'GET':
        print   userdatastore

        return render_template ('public/test1.html')
    else:
        return render_template ('public/signin.html')



@my_view.route ('/start_paypal', methods=['POST'])
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


@my_view.route ("/subscribe", methods=['POST', 'GET'])
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
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


my_view = Blueprint('my_view', __name__ ,template_folder='templates',
                    static_folder='static')
# from models.Usermodel import *
# from models.Usermodel import *

#

@my_view.route ('/', methods=['POST', 'GET'])
def dashmain():
    if request.method == 'GET':
        return render_template('public/index.html')
        # logout_user(user)



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
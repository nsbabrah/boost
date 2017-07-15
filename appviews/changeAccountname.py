
import os
import re
import user


import flask
from flask import Flask, Blueprint, render_template, request, jsonify, g, make_response, redirect, url_for, session, \
    send_from_directory
from paypalrestsdk import Payment
import requests




# from appviews.siginview import my_view
from flask_sqlalchemy import SQLAlchemy
from flask_login import logout_user, login_required, UserMixin,LoginManager

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
# import flask_sqlalchemy
from paypalrestsdk import Payment
import logging



from app import db
import models
import paypalrestsdk
import flask_login

from config import *
from OpenSSL import SSL

userold=None
from approutes import my_view

from models.Usermodel import *

useraccname=0

@my_view.route ('/changeUser', methods=['POST', 'GET'])
def changeAccountname():
    if request.method == 'POST':
        global useraccname
        print request.json
        # useraccname=request.json['name']
        useraccname = request.json['new']
        print useraccname
        global userold
        userold=request.json['old']
        user = models.Usermodel.userpackage.query.filter(models.Usermodel.userpackage.Auto_ac_name == useraccname).first ()

        print user
        if user != None:
            return "False User Already Register"
        # this if statement should be done when payment is recived



        payment = paypalrestsdk.Payment ({
            "intent": "sale",

            # Payer
            # A resource representing a Payer that funds a payment
            # Payment Method as 'paypal'
            "payer": {
                "payment_method": "paypal"},

            # Redirect URLs
            "redirect_urls": {
                "return_url": "http://pythonapps.com:1300/dashboard#/Autoround?success",
                "cancel_url": "http://pythonapps.com:1300/dashboard#/Autoround?failed"},

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

@my_view.route ('/Usernamechanged', methods=['POST', 'GET'])
def paymentpaypalonetime():
    if request.method == 'POST':
        payment_id = request.args.get ('paymentId', None)
        payer_id = request.args.get ('PayerID', None)
        # payer_id = request.args.get('PayerID', None)
        payment = paypalrestsdk.Payment.find(payment_id)
        # billing_agreement_response = BillingAgreement.execute (payment_token)
        # print("BillingAgreement[%s] executed successfully" % billing_agreement_response.id)

        # # print payer_id
        # # print payment_id
        print userold

        if payment.execute({"payer_id": payer_id}):
            payment = paypalrestsdk.Payment.find(payment_id)

            payment_history = paypalrestsdk.Payment.all({"count": 1})
            r = payment_history.payments
            print r
            for i in r:
                # print i['first_name']
                # print i['last_name']
                # print i['int r[0]email']


                status=i['state']
                # print i['create_time']
                if (status == 'approved'):
                    if user == None:
                        print userold
                        userdata = models.Usermodel.userpackage.query.filter_by (Auto_ac_name=userold).first ()
                        userdata.Auto_ac_name = useraccname
                        db.session.add (userdata)
                        db.session.commit ()
                        print "payemt done"



                        return True
                else:
                    return render_template('public/test1.html')

        else:
            return render_template('public/test1.html')





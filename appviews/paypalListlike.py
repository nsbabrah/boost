#Author: Navjot singh Babrah
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
from models.listlike import Listlikes
from paypalrestsdk import BillingPlan, BillingAgreement
import models

from app import db
import paypalrestsdk
import flask_login

from config import *
from OpenSSL import SSL
import siginview
# from siginview import getusername
# print getusername()
from approutes import my_view

@my_view.route ('/start_paypal_listlike', methods=['POST'])
# @cross_origin()
# @auth.verify_password
# @login_required
def startpaypal_listlike():
    if request.method == 'POST':

        username  = request.json['username']
        print username

        billing_plan = BillingPlan ({
            "name":"dd",
            "description": "Create Plan for Regular",
            "merchant_preferences": {
                "auto_bill_amount": "yes",
                "cancel_url": "http://pythonapps.com:1300/dashboard#/Listlike?failed_user",
                "initial_fail_amount_action": "continue",
                "max_fail_attempts": "0",
                "return_url": "http://pythonapps.com:1300/dashboard#/Listlike?success_user"

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


            else:
                print(billing_plan.error)
        else:
            print(billing_plan.error)


@my_view.route ("/subscribe_listlike", methods=['POST', 'GET'])
def subscribe_listlike():
    if request.method == 'POST':
        payment_token=request.json['token']
        o=request.args.get('paymentId')
        # global userdatastore
        # print userdatastore
        # userdatastore = 'dj'
        # print userdatastore
        # payment_id = billing_id


        # billing_agreement_response  = BillingAgreement.execute(payment_token)
        # print billing_agreement_response
        # billing_agreement = BillingAgreement.find (billing_agreement_response.id)
        # print billing_agreement.final_payment_date
        # # transactions = billing_agreement.search_transactions(start_date, end_date)
        # # print transactions
        # print("Got Billing Agreement Details for Billing Agreement[%s]" % (billing_agreement.id))
        # #paypal lislike and autoround payment differentiate below
        #
        # #listlike
        #Autoround
        print request.json
        import json
        # auto_round_name = request.json['username']


        print request.json['userdata']
        r=request.json['userdata']
        t = json.loads(r)




        userdatas=models.listlike.Listlikes()
        LoggedOnUser = flask_login.current_user
        user = LoggedOnUser.username
        print user
        userdatas.user = user
        userdatas.instauser= t['username']
        userdatas.instapass = t['password']
        userdatas.listlikestatus = '0'
        db.session.add(userdatas)
        db.session.commit()
        return 'listlike'







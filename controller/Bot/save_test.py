import urllib
import json
import threading
import ssl
import codecs
import MySQLdb
# # import request
import requests
import time
# # opener = urllib.request.build_opener(
# # urllib.request.ProxyHandler(
# #     {'http': '127.0.0.1:24000'}))
# # connect
#
db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
proxy=['http:127.0.0.1:24000','http:127.0.0.1:24000','http:127.0.0.1:24000','http:127.0.0.1:24000','http:127.0.0.1:24000']
# link=opener.open("http://www.instagram.com/navjotbabrah/?__a=1").read()
# print(link)

autoround_users=['luxuryrumor',
'Tunerlab',
'Bmwm_insta',
'Gojko.lojpur',
'jerseychampsllc',
'thedapperhaus',
'quotes4abundance',
'jae.sohn',
'anguilla_tourism',
'ashleighkwong',
'joergzuber',
'fashionambit',
'billionairemanifesto',
'_worldwidestance_',
'mastermindteam',
'eddiefitot',
'trxblackranks',
'being.charles',
'thezelatakogan',
'elevatedsociety',
'exploreresorts',
'transformationpost',
'allthisfood',
'healthyamazingrecipes',
'healthinspirationforyou',
'Kruetv',
'vendettaluxury',
]

def autoround_update():

    for i in autoround_users:
        reader = codecs.getreader("utf-8")
        context = ssl._create_unverified_context()

        link1=requests.get("https://www.instagram.com/"+"".join(str(i))+"/?__a=1")
        p=(link1.text)
        # print (p)
    db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
    cursor = db.cursor()
    while True:
            # print (p['user']['username'])

            try:


                cursor.execute("INSERT INTO `test`( `name`) VALUES ('crontab')")

                db.commit()
                # time.sleep(2)
            except:
                print "Error"
                db.rollback()
                time.sleep(1)
            db.close()





            # r =['user']['username']
            # print r
            # for i in enumerate(r):
            #     print p[i]
            # a=p['user']['username']
            # print a


            # print (data)
            # a=data['user']['username']UPDATE `user-assigned` SET `username`='1sddrrrrrrs' WHERE id=1


                # a=data['user']['username']
                # print a




            # # get the number of rows in the resultset
            # # numrows = int(cursor.rowcount)
            #
            # print (data['user']['username'])
            # # print (data['user']['post']['count'])
            # print (data['user']['biography'])
            # print (data['user']['follows']['count'])
            # print (data['user']['followed_by']['count'])
            # print (data['user']['profile_pic_url'])
            threading.Timer(399.0, autoround_update).start()
            print ("Updateing AutoRound!")

        # conn = .connect()




autoround_update()
    #
# db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
# curs = db.cursor()
#
# while True:
#     try:
#         curs.execute ("""INSERT INTO thetemps
#                 values(0, CURRENT_DATE(), NOW(), 28)""")
#         db.commit()
#         print "Data committed"
#     except:
#         print "Error"
#         db.rollback()
#     time.sleep(1)
# db.close()

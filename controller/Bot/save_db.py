import urllib
import json
import threading
import ssl
import codecs
import MySQLdb
# import request
import requests
import time
# opener = urllib.request.build_opener(
# urllib.request.ProxyHandler(
#     {'http': '127.0.0.1:24000'}))
# connect

db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
proxy=['http:127.0.0.1:24000','http:127.0.0.1:24000','http:127.0.0.1:24000','http:127.0.0.1:24000','http:127.0.0.1:24000']
# link=opener.open("http://www.instagram.com/navjotbabrah/?__a=1").read()
# print(link)

autoround_users=['davinderbhullar_90','gagan_babrah_7860','navjotbabrah','jeffrr111111','luxury.lifes','jaideep085','bendale009','jonathananthan','pavitar_chhina_','deep3214']
def autoround_update():
    for i in autoround_users:
        cursor = db.cursor()
        reader = codecs.getreader("utf-8")

        # conn = .connect()


        context = ssl._create_unverified_context()

        link1=requests.get("https://www.instagram.com/"+"".join(str(i))+"/?__a=1")
        p=(link1.text)
        print json.loads(p)
        # time.sleep(2)
        cursor.execute("INSERT INTO `user-assigned`(`username`) VALUES ('qweqw')")

        db.commit()
        time.sleep(2)

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
        threading.Timer(499.0, autoround_update).start()
        print ("Updateing AutoRound!")

autoround_update()
    #

import urllib
import json
import threading
import ssl
import codecs
# import MySQLdb
# import request
import urllib.request
# opener = urllib.request.build_opener(
# urllib.request.ProxyHandler(
#     {'http': '127.0.0.1:24000'}))
# connect
# db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
proxy=['127.0.0.1:24000','127.0.0.1:24000','127.0.0.1:24000','127.0.0.1:24000','127.0.0.1:24000']
# link=opener.open("http://www.instagram.com/navjotbabrah/?__a=1").read()
# print(link)
autoround_users=['davinderbhullar_90','gagan_babrah_7860','navjotbabrah','jeffrr111111','luxury.lifes','jaideep085','bendale009','jonathananthan','pavitar_chhina_','deep3214']
def autoround_update():
    for i,r in zip(autoround_users,proxy):
        reader = codecs.getreader("utf-8")

        context = ssl._create_unverified_context()

        link1=urllib.request("https://nsbabrahapp.herokuapp.com").read().json('utf-8')
        link=(link1)


        data = (link)
        # print (data)
        # a=data['user']['username']
        # # cursor.execute("INSERT INTO (`username`) Values (1)")
        # # add_employee =("INSERT * STUDENT(name) VALUES(a)")
        # # db.commit()
        #
        # # get the number of rows in the resultset
        # # numrows = int(cursor.rowcount)
        #
        # print (data['user']['username'])
        # # print (data['user']['post']['count'])
        # print (data['user']['biography'])
        # print (data['user']['follows']['count'])
        # print (data['user']['followed_by']['count'])
        # print (data['user']['profile_pic_url'])
        threading.Timer(59.0, autoround_update).start()
        print ("Updateing AutoRound!")

autoround_update()
    #

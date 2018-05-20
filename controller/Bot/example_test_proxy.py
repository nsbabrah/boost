# # import urllib
# import json
# import threading
# # from flask import Flask
# import MySQLdb
# import time
# import requests
#
# proxy=['127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34002']
# ip = "0.0.0.0:9878"
# boostlikes_users=['davinderbhullar_90','gagan_babrah_7860','navjotbabrah','jeffrr111111','luxury.lifes','jaideep085','jonathananthan','davidryan0','navbbarnad','manpreetsingh8750','bennuttan','samra1850','pavitar_chhina_','deep321','maninderbhatti50','shoppingbird_asr','aulakh4235','harshgill0786','gurbir3195','samakshvanmolly','jagrooppb02','love____struck','sudhir_chodhary','gurtaj1996','viren_galaxy','bhullar_rajwant','vickybhullar786','jassisakhira','psgaganpb02','daljit.singh666','ramdeep16','deepakthakur3003','hemaantarora','jatt_personality','dr_nickx','hrmn_sndhu7','jaibeer_singh_chhina','chhinaharry30','maannavtej','ayesha_i___9','s_andhu6','sidhumantri','sharmamayan','simran_bhullar_','suhail_19_','patrick.k.wong','gupta_api','gurvir_sandhu1','gurkaran7575','amritbir.singh.39','966miguel','joban_chhina','aarav_sharmaarav']
#
# # print(opener.open('https://www.instagram.com/gagan_babrah_7860/?__a=1').read())
# d=0
# def userprofile_info():
#     for i in boostlikes_users:
#
#         # scrape=requests.Session()
#         link=requests.get("http://www.instagram.com/"+"".join(str(i))+"/?__a=1" ,proxies={'http':'http://127.0.0.1:22225'})
#         link1=requests.get("http://lumtest.com/myip.json" ,proxies={'http':'http://127.0.0.1:22225'})
#         j=json.loads(link1.content)
#         print j
#         # link = "https://www.instagram.com/gagan_babrah_7860/?__a=1"
#         # f = requests.get(link,proxies={'http': 'http://10.11.4.254:3128'})
#         myfile = (link.content)
#
#         data = json.loads(myfile)
#         print (data['user']['username'])
#         # print r[0]['likes']['count']
#         # print r[0]['comments']['count']
#
#         # cursor.execute("INSERT INTO `test`(`name`) VALUES ('as')")
#
#         # db.commit()
#
#         # print (data['user']['username'])
#         # # # print (data['user']['post']['count'])
#         # # print (data['user']['biography'])
#         # # print (data['user']['follows']['count'])
#         # # print (data['user']['followed_by']['count'])
#         # # print (data['user']['profile_pic_url'])
#         # r=data['user']['media']['nodes']
#         # try:
#         #     if len(r) < 1:
#         #         print  (0)
#         #         # cursor.execute("INSERT INTO `test`(`name`) VALUES (%s)"% (r[0]['likes']['count']) )
#         #         #
#         #         # db.commit()
#         #         print (data['user']['username'])
#         #         # print r[0]['likes']['count']
#         #         # print r[0]['comments']['count']
#         #
#         #         # cursor.execute("INSERT INTO `autoround`(`username`) VALUES ('as1')")
#         #         #
#         #         # db.commit()
#         #         continue
#         #     else:
#         #         print (data['user']['username'])
#         #         print r[0]['likes']['count']
#         #         print r[0]['comments']['count']
#         #
#         #         cursor.execute("INSERT INTO `test`(`name`) VALUES ('as')")
#         #
#         #         db.commit()
#         #     # time.sleep(2)                            # time.sleep(2)
#         # except:
#         #     print "Error"
#         #     # db.rollback()
#         #     time.sleep(1)
#         #     continue
#         #     # db.close()
#
#
#
#         # # need to change thread time 3 time per day
#         # print ("Recent Images!")
#         # # requests.urlretrieve(''.join(data['user']['profile_pic_url']),"user_info/profile_img/"+"".join(str(i))+".jpg")
#
#         # print 'asasa'
#         threading.Timer(39.0, userprofile_info).start()
# # db.close()
#
# # db.close()
#         # print r
#
#
#
#
# userprofile_info()
#
#
#
#
#     # for i in autoround_users:
#     #     reader = codecs.getreader("utf-8")
#     #     context = ssl._create_unverified_context()
#     #
#     #     link1=requests.get("https://www.instagram.com/"+"".join(str(i))+"/?__a=1")
#     #     p=(link1.text)
#     #     print (p)
#                 # db.close()SET GLOBAL max_connections = 1024;
#         # db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
#         # cursor = db.cursor()
#
#
#
#
# # # params = urllib.urlencode(post_params)
# import urllib
import json
import threading
# from flask import Flask
from crontab import CronTab

import MySQLdb
import time
import requests
from datetime import date
import sched
s = sched.scheduler(time.time, time.sleep)
proxy=['127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34002']
ip = "0.0.0.0:9878"
boostlikes_users=[]

# print(opener.open('https://www.instagram.com/gagan_babrah_7860/?__a=1').read())
d=0
# empty_cron = CronTab()
# my_user_cron = CronTab(user=True)
# users_cron = CronTab(user='navjotbabrah')
#
# system_cron = CronTab(tabfile='save_proxy.py', user=False)
# job = system_cron[0]
# job.user != None
# system_cron.new(command='python', user='root')
# job.minute.during(1,50).every(1)
def userprofile_info(sc):
    for i in boostlikes_users:

        # print i
        # time.sleep(2)

        db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
        cursor = db.cursor()

        # scrape=requests.Session(3
        link=requests.get("http://www.instagram.com/"+"".join(str(i))+"/?__a=1" ,proxies={'http':'http://127.0.0.1:22225'})
        link1=requests.get("http://lumtest.com/myip.json" ,proxies={'http':'http://127.0.0.1:22225'})
        j=json.loads(link1.content)
        print j
        # link = "https://www.instagram.com/gagan_babrah_7860/?__a=1"
        # f = requests.get(link,proxies={'http': 'http://10.11.4.254:3128'})
        myfile = (link.content)

        data = json.loads(myfile)
        print (data['user']['username'])
        cursor.execute("INSERT INTO `data`(`data`) VALUES ('234')")
        db.commit()
        print threading.active_count()
        # threading.Timer(3.0, userprofile_info).start()
        # threading.Timer(3, self.update).start()
        s.enter(30, 1, userprofile_info, (sc,))
        # threading.shutdown = True


    # for i in autoround_users:
    #     reader = codecs.getreader("utf-8")
    #     context = ssl._create_unverified_context()
    #
    #     link1=requests.get("https://www.instagram.com/"+"".join(str(i))+"/?__a=1")
    #     p=(link1.text)
    #     print (p)
                # db.close()SET GLOBAL max_connections = 1024;

        # db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
        # cursor = db.cursor()


                # # # print (data['user']['post']['count'])
                # # print (data['user']['biography'])
                # # print (data['user']['follows']['count'])
                # # print (data['user']['followed_by']['count'])
                # # print (data['user']['profile_pic_url'])
                # r=data['user']['media']['nodes']
#                 try:
#
#                         if len(r) < 1:
#                             print  (0)
#                             # cursor.execute("UPDATE `autoround` SET username=(%s) WHERE username=(%s);",(data['user']['username']),(data['user']['username']))
#                             cursor.execute("INSERT INTO `autoround`(`username`) VALUES ('as1dsadsd')")
#                             db.commit()
#                             print (data['user']['username'])
#                             print r[0]['likes']['count']
#                             print r[0]['comments']['count']
#
#                             # cursor.execute("INSERT INTO `autoround`(`username`) VALUES ('as1')")
#
#                             # db.commit()
#                             continue
#                         else:
#                             print (data['user']['username'])
#                             print r[0]['likes']['count']
#                             print r[0]['comments']['count']
# #
#                             # cursor.execute("INSERT INTO `autoround`(`username`) VALUES ('as')")
#
#                             # db.commit()
#                         # time.sleep(2)
#                 except:
#                     print "Error"
#                     # db.rollback()
#                     time.sleep(1)
#                     # db.close()
#
#

                # # need to change thread time 3 time per day
                # print ("Recent Images!")
                # # requests.urlretrieve(''.join(data['user']['profile_pic_url']),"user_info/profile_img/"+"".join(str(i))+".jpg")

                # print 'asasa'

        # db.close()
                # print r



s.enter(30, 1, userprofile_info, (s,))
while True:
    try:
        s.run()
    except:
        print 'Error'
        continue
# userprofile_info()


# # params = urllib.urlencode(post_params)

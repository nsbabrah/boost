import urllib
import json
import threading
# from flask import Flask
import MySQLdb
import time

proxy=['127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34002']
ip = "0.0.0.0:9878"
boostlikes_users=['gagan_babrah_7860','navjotbabrah','jeffrr111111','luxury.lifes','jaideep085','jonathananthan','davidryan0','navbbarnad','manpreetsingh8750','bennuttan','samra1850','pavitar_chhina_','deepakthakur3003']
# print(opener.open('https://www.instagram.com/gagan_babrah_7860/?__a=1').read())
d=0
def userprofile_info():

    # for i in autoround_users:
    #     reader = codecs.getreader("utf-8")
    #     context = ssl._create_unverified_context()
    #
    #     link1=requests.get("https://www.instagram.com/"+"".join(str(i))+"/?__a=1")
    #     p=(link1.text)
    #     print (p)
                # db.close()

        db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
        cursor = db.cursor()
        while True:
            for i in boostlikes_users:
                link=("https://www.instagram.com/"+"".join(str(i))+"/?__a=1").decode('utf-8')
                # link = "https://www.instagram.com/gagan_babrah_7860/?__a=1"SET GLOBAL max_connections = 1024;
                f = urllib.urlopen(link)
                myfile = f.read()

                data = json.loads(myfile)
                # print (data['user']['username'])
                # # print (data['user']['post']['count'])
                # print (data['user']['biography'])
                # print (data['user']['follows']['count'])
                # print (data['user']['followed_by']['count'])
                # print (data['user']['profile_pic_url'])
                r=data['user']['media']['nodes']
                try:
                    

                        if len(r) < 1:
                            print  (0)
                            # cursor.execute("INSERT INTO `test`(`name`) VALUES (%s)"% r[0]['likes']['count'] )

                            # db.commit()
                            print (data['user']['username'])
                            print r[0]['likes']['count']
                            print r[0]['comments']['count']

                            cursor.execute("INSERT INTO `autoround`(`username`) VALUES ('as1')")

                            db.commit()
                            continue
                        else:
                            print (data['user']['username'])
                            print r[0]['likes']['count']
                            print r[0]['comments']['count']

                            cursor.execute("INSERT INTO `autoround`(`username`) VALUES ('as')")

                            db.commit()
                        # time.sleep(2)
                except:
                    print "Error"
                    # db.rollback()
                    time.sleep(1)
                    # db.close()



                # need to change thread time 3 time per day
                print ("Recent Images!")
                urllib.urlretrieve(''.join(data['user']['profile_pic_url']),"user_info/profile_img/"+"".join(str(i))+".jpg")


                threading.Timer(339.0, userprofile_info).start()
        db.close()
                # print r




userprofile_info()


# # params = urllib.urlencode(post_params)



#Author: Navjot Singh Babrah

from selenium import webdriver
#from instagram.client import InstagramAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,sched
import sched
import MySQLdb
s = sched.scheduler(time.time, time.sleep)
username = "jeffrr111111"
password = "jeff1234"
target='gagan_babrah_7860'
target1='jeffrr111111'
# time.sleep(3)


PROXY = "64.57.141.2:60000" # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34002" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34003" # IP:PORT or HOST:PORT
# listlike
paid_user=['jeffrr111111','jonathananthan','davidryan0']
password=['jeff1234','tigerisback','therockiscooking']
proxy=['https:https://rodrigom:Ub3neQZ5vx@64.57.141.11:60000']
poxy = {'https': 'https://rodrigom:Ub3neQZ5vx@64.57.141.11:60000'}

headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, /',

'Accept-Encoding': 'gzip, deflate',

'Accept-Language': 'en-US, en; q=0.7',

'Connection': 'Keep-Alive',

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}


# response = requests.get('https://nsbabrahapp.herokuapp.com', headers=headers, proxies = proxy)
#


# target=['manpreetsingh8750','bennuttan','samra1850','pavitar_chhina_','deep3214']
target=['gagan_babrah_7860',
'luxuryrumor',
'Tunerlab',
'Bmwm_insta',
'Gojko.lojpur',
'jerseychampsllc',
'thedapperhaus',
'quotes4abundance',
]
i=0
# d=0
p1=[1,2,3,4,5,6,7,8,9,10]
u1=0




# chrome_options.add_argument('--proxy-server=http://%s' % PROXY1)
#
#
# chrome = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")

def userprofile_info(sc):
    for u,p,r,i in zip(paid_user,password,proxy,target):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('%s' % poxy )


#../../usr/local/bin/chromedriver      for cron tab
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        dd1 = ("https://www.instagram.com/accounts/login/")
        driver1 = chrome
        driver1.get(dd1)
        time.sleep(2)

        # s.enter(1, 10, userprofile_info, (sc,))




        try:



            db.commit()
            driver1.find_element_by_xpath("//input[@name='username']").send_keys("".join(str(u)))
            driver1.find_element_by_xpath("//input[@name='password']").send_keys("".join(str(p)))


            driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
            time.sleep(2)


        except:
            continue

        print(p, u,r,i)
        d=0

        for i in target:
            print i

            if (d <=len(target)):
                url=  ("https://www.instagram.com/"+ "".join(str(i)))
                dd1 = url
                driver1 = chrome
                driver1.get(dd1)
                time.sleep(1)


                try:
                    driver1.find_element_by_css_selector('._ovg3g').click()
                    # driver2.get(dd1)
                    # driver2= chrome
                    # driver2.find_element_by_css_selector('._ovg3g').click()
                    time.sleep(3)
                except:
                    continue

                try:
                    time.sleep(2)
                    driver1.find_element_by_xpath("//span[contains(.,'Like')]").click()
                    # driver2.find_element_by_xpath("//span[contains(.,'Like')]").click()
                except:
                    try:
                        driver1.find_element_by_css_selector('._3eajp').click()
                        # driver2.find_element_by_css_selector('._3eajp').click()
                        print(driver1.get('https://lumtest.com/myip.json'))
                    except:
                        continue
                        # s.enter(6, 1, userprofile_info, (sc,))

s.enter(1, 1, userprofile_info, (s,))
# s.run()
s.run()
while True:
    try:
        s.run()

    except:
        print 'Error'
        continue



            # if(i[-2]):
            #      try:
            #        driver1.quit()
            #      #   continue
            #      except:
            #          print 'err'
            #      #   continue
            #



                    # driver1.quit()

                # s.enter(6, 1, userprofile_info, (sc,))










  # time.sleep(4)
        # s.enter(6, 1, userprofile_info, (sc,))






                    # driver1.find_element_by_css_selector('._phrgb').click() for follow
                # time.sleep(3)
                # while True:
                #     try:
                #         print(driver1.get('https://lumtest.com/myip.json'))
                #         time.sleep(4)
                #         s.enter(6, 1, userprofile_info, (sc,))
                #
                #
                #     except:
                #         # driver1.find_element_by_css_selector('._3eajp').click()
                #         time.sleep(2)
                #         s.enter(6, 1, userprofile_info, (sc,))







                # driver1.find_element_by_css_selector('._soakw ._vbtk2 ').click()

#
#
# def userprofile_info1(sc):
#     for u,p,r,i,a in zip(paid_user,password,proxy,target,p1):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=http://%s' % r)
#
#
#         chrome = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")
#         dd1 = ("https://www.instagram.com/accounts/login/")
#         driver1 = chrome
#         driver1.get(dd1)
#         time.sleep(2)
#
#         # s.enter(1, 10, userprofile_info, (sc,))
#
#
#
#
#         try:
#             driver1.find_element_by_xpath("//input[@name='username']").send_keys("".join(str(u)))
#             driver1.find_element_by_xpath("//input[@name='password']").send_keys("".join(str(p)))
#
#
#             driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
#             time.sleep(2)
#
#
#         except:
#             continue
#
#         print(p, u,r,i)
#         d=0
#
#         for i in target:
#             print i
#
#             if (d <=len(target)):
#                 url=  ("https://www.instagram.com/"+ "".join(str(i)))
#                 dd1 = url
#                 driver1 = chrome
#                 driver1.get(dd1)
#                 time.sleep(1)
#
#
#                 try:
#                     driver1.find_element_by_css_selector('._ovg3g').click()
#                     # driver2.get(dd1)
#                     # driver2= chrome
#                     # driver2.find_element_by_css_selector('._ovg3g').click()
#                     time.sleep(3)
#                 except:
#                     continue
#
#                 try:
#                     time.sleep(2)
#                     driver1.find_element_by_xpath("//span[contains(.,'Like')]").click()
#                     # driver2.find_element_by_xpath("//span[contains(.,'Like')]").click()
#                 except:
#                     try:
#                         driver1.find_element_by_css_selector('._3eajp').click()
#                         # driver2.find_element_by_css_selector('._3eajp').click()
#                         print(driver1.get('https://lumtest.com/myip.json'))
#                     except:
#                         continue
#                         # s.enter(6, 1, userprofile_info, (sc,))
#
#
#
#
#
#
#
#
#
#
#
# s.enter(1, 1, userprofile_info, (s,))
# # s.run()
# s.run()
# while True:
#     try:
#         s.run()
#     except:
#         print 'Error'
#         continue
#
#
#
# # d+=1
#







# https://www.instagram.com/jeffrr111111/?__a=1    use to get user info as url







# "x%d"%i = data[:,i-1]


# r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
# driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target1)
# print params['o']
# wait = WebDriverWait(driver1, 20)
# driver1.find_element_linktext('/navjotbabrah/').click()  'gagan_babrah_7860','jeffrr111111','davinderbhullar_90',

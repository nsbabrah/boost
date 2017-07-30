

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

s = sched.scheduler(time.time, time.sleep)
username = "jeffrr111111"
password = "jeff1234"
target='gagan_babrah_7860'
target1='jeffrr111111'
# time.sleep(3)


PROXY = ["64.57.141.2:60000"] # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34002" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34003" # IP:PORT or HOST:PORT
# listlike
paid_user=['jeffrr111111']
password=['jeff1234']
# proxy=['https:https://rodrigom:Ub3neQZ5vx@64.57.141.11:60000']
poxy = {'https': 'https://rodrigom:Ub3neQZ5vx@64.57.141.11:60000'}



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

def userprofile_start():
    for u,p,r,i in zip(paid_user,password,PROXY,target):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('%s' % poxy )


#../../usr/local/bin/chromedriver      for cron tab
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        dd1 = ("https://www.instagram.com/accounts/login/")
        driver1 = chrome
        driver1.get(dd1)
        time.sleep(2)

        try:

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
    driver1.quit()

# s.enter(1, 1, userprofile_start,())
# s.run()
#
# while True:
#     try:
#         s.run()
#
#     except:
#         print 'Error'
#         continue
#

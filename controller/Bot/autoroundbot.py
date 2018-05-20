

#Author: Navjot Singh Babrah
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,sched
import sched
s = sched.scheduler(time.time, time.sleep)
username = ""
password = ""
target=''
target1=''
# time.sleep(3)


PROXY = "127.0.0.1:34005" # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34002" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34003" # IP:PORT or HOST:PORT

paid_user=['jonathananthan','davidryan0']
password=['tigerisback','therockiscooking']
proxy=['127.0.0.1:34002','127.0.0.1:34003','127.0.0.1:34002','127.0.0.1:34002','127.0.0.1:34003']

# target=['manpreetsingh8750','bennuttan','samra1850','pavitar_chhina_','deep3214']
target=[
]

i=0
# d=0
p1=0
u1=0




# chrome_options.add_argument('--proxy-server=http://%s' % PROXY1)
#
#
# chrome = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")

def userprofile_info(sc):
    for u,p,r,i in zip(paid_user,password,proxy,target):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % r)

        chrome = webdriver.Chrome(chrome_options=chrome_options)
        dd1 = ("https://www.instagram.com/accounts/login/")
        driver1 = chrome
        driver1.get(dd1)
        try:
            driver1.find_element_by_xpath("//input[@name='username']").send_keys("".join(str(u)))
            driver1.find_element_by_xpath("//input[@name='password']").send_keys("".join(str(p)))


            driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()

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
                try:
                    driver1.find_element_by_css_selector('._ovg3g').click()
                    time.sleep(3)
                except:
                    continue

                try:
                    driver1.find_element_by_xpath("//span[contains(.,'Like')]").click()
                except:
                    driver1.find_element_by_css_selector('._3eajp').click()
                    print(driver1.get('https://lumtest.com/myip.json'))

                    # s.enter(6, 1, userprofile_info, (sc,))
            if(i[-2]):
                 try:
                   driver1.quit()
                 #   continue
                 except:
                     print 'err'
                 #   continue





                # driver1.find_element_by_css_selector('._soakw ._vbtk2 ').click()












s.enter(1, 1, userprofile_info, (s,))
# s.run()
s.run()
while True:
    try:
        s.run()
    except:
        print 'Error'
        continue



# d+=1
#







# https://www.instagram.com/jeffrr111111/?__a=1    use to get user info as url







# "x%d"%i = data[:,i-1]


# r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
# driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target1)
# print params['o']
# wait = WebDriverWait(driver1, 20)
# driver1.find_element_linktext('/navjotbabrah/').click()  'gagan_babrah_7860','jeffrr111111','davinderbhullar_90',

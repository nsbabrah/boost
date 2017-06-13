

#Author: Navjot Singh Babrah
from selenium import webdriver
from instagram.client import InstagramAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,sched

username = "jhondigg009"
password = "jhondigg1234"
target='gagan_babrah_7860'
target1='jeffrr111111'
# time.sleep(3)


PROXY = "127.0.0.1:34005" # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34002" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34003" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
#
chrome_options.add_argument('--proxy-server=http://%s' % PROXY2)

chrome = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")

dd1 = ("https://www.instagram.com/accounts/login/")
driver1 = chrome
driver1.get(dd1)
driver1.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver1.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(3)
i=0

# "x%d"%i = data[:,i-1]


# r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
# driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target1)
# print params['o']
# wait = WebDriverWait(driver1, 20)
# driver1.find_element_linktext('/navjotbabrah/').click()  'gagan_babrah_7860','jeffrr111111','davinderbhullar_90',
time.sleep(4)
d=0
target=['jeffrr111111','gagan_babrah_7860','davinderbhullar_90','luxury.lifes']

for i in target:
    if (d!=len(target)):
        url=  ("https://www.instagram.com/"+ "".join(str(i)))

        dd1 = url
        driver1 = chrome
        driver1.get(dd1)
        driver1.find_element_by_css_selector('._ovg3g').click()
        time.sleep(6)
        # p=driver1.find_elements_by_xpath("//span[contains(text(), 'Like')]")


        driver1.find_element_by_xpath("//span[contains(.,'Like')]").click()


    # driver1.find_element_by_css_selector('._phrgb').click() for follow
        time.sleep(4)
        driver1.find_element_by_css_selector('._3eajp').click()
        time.sleep(4)

# driver1.find_element_by_css_selector('._soakw ._vbtk2 ').click()
        print(driver1.get('https://lumtest.com/myip.json'))
        time.sleep(4)
        d+1
#
#s = sched.scheduler(time.time, time.sleep)
#
#

## opener = urllib.request.build_opener(
##                                      urllib.request.ProxyHandler(
##                                                                  {'https':'https://127.0.0.1:34004'}))
## chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
##
## chrome = webdriver.Chrome(chrome_options=chrome_options)
## getdriver =("http://whatismyipaddress.com")
## chrome.get("http://whatismyipaddress.com")
## driver = webdriver.Chrome()
## driver.get(getdriver)
## driver.get(getdriver)
##
#
## def do_something(sc):
##     username = "jeffrr111111"
##     password = "jeff1234"
##     target='navbabrah'
##     # time.sleep(3)
##
##     dd = ("https://www.instagram.com/accounts/login/")
##     driver = chrome
##     driver.get(dd)
##
##
##     driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
##     driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
##     driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
##     time.sleep(3)
##
##     r=driver.find_element_by_xpath("//div[@class='_a1rcs']").click()
##     driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
##     # wait = WebDriverWait(driver, 20)
##     #////////////////////////////////////////////
##     # # driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
##     # time.sleep(4)
##     # age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._oluat")))
##     # age.click()
##     # time.sleep(4)
##     # age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._phrgb")))
##     # age1.click()
##     print(driver.get('https://lumtest.com/myip.json'))
##     s.enter(10, 1, do_something, (sc,))
##
## s.enter(10, 1, do_something, (s,))
## s.run()
## def doo_something(sc):
#def botstart():
#    username = "jeffrr111111"
#    password = "jeff1234"
#    target=['navbabrah','navjotbabrah']
#    # time.sleep(3)
#    chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
#
#    chrome = webdriver.Chrome(chrome_options=chrome_options)
#
#    dd1 = ("https://www.instagram.com/accounts/login/")
#    driver1 = chrome
#    driver1.get(dd1)
#    driver1.find_element_by_xpath("//input[@name='username']").send_keys(username)
#    driver1.find_element_by_xpath("//input[@name='password']").send_keys(password)
#    driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
#    time.sleep(3)
#    i=0
#
#    # "x%d"%i = data[:,i-1]
#
#
#    r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
#    driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
#    # wait = WebDriverWait(driver, 20)
#    # driver1.find_element_linktext('/navjotbabrah/').click()
#time.sleep(4)
#dd1 = ("https://www.instagram.com/navbabrah/")
#driver1 = chrome
#driver1.get(dd1)
#driver1.find_element_by_css_selector('._phrgb').click()
#time.sleep(4)
#print(driver1.get('https://lumtest.com/myip.json'))
## i+=1
## wait = WebDriverWait(driver1, 10)
## langselction = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "_phrgb")))
## langselction.click()
## driver1.find_element_by_css_selector('._q6fzq').click()
#    #////////////////////////////////////////////
#    # # driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
#    # time.sleep(4)
#    # age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._oluat")))
#    # age.click()
#    # time.sleep(4)
#    # age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._phrgb")))
#    # age1.click()
#    print(driver1.get('https://lumtest.com/myip.json'))
#    # s.enter(30, 1, doo_something, (sc,))
#
## s.enter(30, 1, doo_something, (s,))
## s.run()

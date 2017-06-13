##!/usr/bin/env python
#print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
#    'YOURPASS, please contact sales@luminati.io')
#import urllib.request
#import random
#username = 'lum-customer-pietro-zone-residential'
#password = '97f70168673d'
#port = 22225
#session_id = random.random()
#super_proxy_url = ('http://%s-country-us-session-%s:%s@zproxy.luminati.io:%d' %
#    (username, session_id, password, port))
#proxy_handler = urllib.request.ProxyHandler({
#    'http': super_proxy_url,
#    'https': super_proxy_url,
#})
#opener = urllib.request.build_opener(proxy_handler)
#print('Performing request')
#print(opener.open('http://lumtest.com/myip.json').read())
# import urllib.request
from selenium import webdriver
from instagram.client import InstagramAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
username = "jeffrr111111"
password = "jeff1234"
target='navjotbabrah'
time.sleep(3)


PROXY = "127.0.0.1:34005" # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34000" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34006" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
#
# opener = urllib.request.build_opener(
#                                      urllib.request.ProxyHandler(
#                                                                  {'https':'https://127.0.0.1:34004'}))
chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
# getdriver =("http://whatismyipaddress.com")
# chrome.get("http://whatismyipaddress.com")
# driver = webdriver.Chrome()
# driver.get(getdriver)
# driver.get(getdriver)
#
dd = ("https://www.instagram.com/accounts/login/")
driver = chrome
driver.get(dd)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(3)

r=driver.find_element_by_xpath("//div[@class='_a1rcs']").click()
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
wait = WebDriverWait(driver, 2)
#////////////////////////////////////////////
# driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
time.sleep(2)
# age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._a1rcs")))
# age.click()
time.sleep(4)
age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._a1rcs")))
age1.click()

# age2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._q8rex")))
# age2.click()
# /////////////////First proxy workerd till here ////////////////////////////////
PROXY1 = "127.0.0.1:34000" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34006" # IP:PORT or HOST:PORT

chrome_options.add_argument('--proxy-server=http://%s' % PROXY1)

chrome = webdriver.Chrome(chrome_options=chrome_options)
username = "jakeshefler1"
password = "jake1234"
target='navjotbabrah'
time.sleep(8)
dd = ("https://www.instagram.com/accounts/login/")
driver = chrome
driver.get(dd)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(6)

r=driver.find_element_by_xpath("//div[@class='_a1rcs']").click()
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
wait = WebDriverWait(driver, 20)
#////////////////////////////////////////////
# driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
time.sleep(2)
age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._a1rcs")))
age.click()
time.sleep(4)
age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._k2vj6")))
age1.click()

age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._tk4ba")))
age1.click()









# chrome.find_element_by_xpath("//input[@name='username']").send_keys(username)
# chrome.find_element_by_xpath("//input[@name='password']").send_keys(password)
# chrome.find_element_by_xpath("//button[contains(.,'Log in')]").click()
# time.sleep(3)
#
# r=chrome.find_element_by_xpath("//input[@class='_t1y9a']").click()
# chrome.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
# wait = WebDriverWait(chrome, 20)
# #////////////////////////////////////////////
# # driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
# time.sleep(4)
# age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._o1o4h")))
# age.click()
# time.sleep(4)
# age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._ovg3g")))
# age1.click()
#
# age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._tk4ba")))
# age1.click()
#
# print(opener.open('https://instagram.com/').read())
# print(opener.open('https://lumtest.com/myip.json').read())
# #

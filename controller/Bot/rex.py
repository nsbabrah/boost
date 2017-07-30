import requests
from selenium import webdriver
#from instagram.client import InstagramAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,sched
import sched
from selenium.webdriver.common.proxy import *
import MySQLdb

proxy = {'http://216.10.7.197:3199'}
sproxy  = {'https': 'https://boostlikes-8wawl:nLXfMKzV6h@216.10.7.197:3199'}
ftp_proxy   = "216.10.7.197:3199"
from selenium import webdriver
PROXY = "31.28.244.230:41905"

headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, /',

'Accept-Encoding': 'gzip, deflate',

'Accept-Language': 'en-US, en; q=0.7',

'Connection': 'Keep-Alive',

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
#
# response = requests.get('https://nsbabrahapp.herokuapp.com', headers=headers, proxies = proxy)
# print response
# import json
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://boostlikes-8wawl:nLXfMKzV6h@%s'% proxy )
# chrome_options.add_argument("ignore-certificate-errors");
# ttp://boostlikes-8wawl:nLXfMKzV6h@
#../../usr/local/bin/chromedriver      for cron tab
chrome = webdriver.Chrome(chrome_options=chrome_options)
# dd1 = ("https://www.instagram.com/accounts/login/")
dd1 = ("https://lumtest.com/myip.json")
driver1 = chrome
driver1.get(dd1)
time.sleep(2)
driver1.quit();
# s.enter(1, 10, userprofile_info, (sc,))




try:

    # cursor.execute("INSERT INTO `test`( `name`) VALUES ('crontab')")


    driver1.find_element_by_xpath("//input[@name='username']").send_keys("".join(str(u)))
    driver1.find_element_by_xpath("//input[@name='password']").send_keys("".join(str(p)))


    driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    time.sleep(2)


except:
    print 'assgygyugyg'

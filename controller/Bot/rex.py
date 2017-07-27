from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

proxy = {'address': 'boostlikes-8wawl:nLXfMKzV6h@216.10.7.197:3199',
         'username': 'boostlikes-8wawl',
         'password': 'nLXfMKzV6h'}


capabilities = dict(DesiredCapabilities.CHROME)
capabilities['proxy'] = {'proxyType': 'MANUAL',
                         'httpProxy': proxy['address'],
                         'ftpProxy': proxy['address'],
                         'sslProxy': proxy['address'],
                         'noProxy': '',
                         'class': "org.openqa.selenium.Proxy",
                         'autodetect': False}

capabilities['proxy']['socksUsername'] = proxy['username']
capabilities['proxy']['socksPassword'] = proxy['password']

driver = webdriver.Chrome( desired_capabilities=capabilities)
driver.get('http://www.whatsmyip.org/')
# import requests
# from selenium import webdriver
# #from instagram.client import InstagramAPI
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import time,sched
# import sched
# from selenium.webdriver.common.proxy import *
# import MySQLdb
#
# ssproxy = 'http://boostlikes-8wawl:nLXfMKzV6h@216.10.7.197:3199'
# sproxy  = {'https': 'https://boostlikes-8wawl:nLXfMKzV6h@216.10.7.197:3199'}
# ftp_proxy   = "boostlikes-8wawl:nLXfMKzV6h@216.10.7.197:3199"
# from selenium import webdriver
# PROXY = "31.28.244.230:41905"
#
# webdriver.DesiredCapabilities.CHROME['proxy']={
# "httpProxy":ftp_proxy,
# "ftpProxy":ftp_proxy,
# "sslProxy":ftp_proxy,
# "noProxy":None,
# "proxyType":"MANUAL",
# "autodetect":False
#
#      }
#
# driver = webdriver.Chrome()
# driver.get('http://www.whatsmyip.org/')
# # proxy = Proxy({
# #     'proxyType': ProxyType.MANUAL,
# #     'httpProxy': ftp_proxy, # set this value as desired
# #     'ftpProxy': ftp_proxy,  # set this value as desired
# #     'sslProxy': ftp_proxy,  # set this value as desired
# #     'noProxy': '',         # set this value as desired
# #     'socksUsername': 'boostlikes-8wawl',
# #     'socksPassword':  'nLXfMKzV6h'
# #     })
# #
# #
# #
# # headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, /',
# #
# # 'Accept-Encoding': 'gzip, deflate',
# #
# # 'Accept-Language': 'en-US, en; q=0.7',
# #
# # 'Connection': 'Keep-Alive',
# #
# # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
# # #
# # # response = requests.get('https://nsbabrahapp.herokuapp.com', headers=headers, proxies = proxy)
# # # print response
# # import json
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--proxy-server=http://%s'% proxy )
# #
# # db = MySQLdb.connect(host="127.0.0.1",port=3307, user="boostlikes", passwd="boostlikes",db='Boostlikes')
# # cursor = db.cursor()
# #
# # #../../usr/local/bin/chromedriver      for cron tab
# # chrome = webdriver.Chrome(chrome_options=chrome_options)
# # # dd1 = ("https://www.instagram.com/accounts/login/")
# # dd1 = ("https://nsbabrahapp.herokuapp.com")
# # driver1 = chrome
# # driver1.get(dd1)
# # time.sleep(2)
# #
# # # s.enter(1, 10, userprofile_info, (sc,))
# #
# #
# #
# #
# # try:
# #
# #     # cursor.execute("INSERT INTO `test`( `name`) VALUES ('crontab')")
# #
# #     db.commit()
# #     driver1.find_element_by_xpath("//input[@name='username']").send_keys("".join(str(u)))
# #     driver1.find_element_by_xpath("//input[@name='password']").send_keys("".join(str(p)))
# #
# #
# #     driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
# #     time.sleep(2)
# #
# #
# # except:
# #     print 'assgygyugyg'

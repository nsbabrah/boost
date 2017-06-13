from selenium import webdriver
import time
PROXY = 'http://127.0.0.1:34005'# IP:PORT or HOST:PORT
PROXY1 = "192.168.2.56" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://127.0.0.1/pcrecords/index.php")

time.sleep(5)
    # You need to put some time sleep in program to act like user
    # bot need to see notification
    # databse set usage 1 on first use of i[p]
    # databse 2nd usage ip same activity half change
    # big data
    # collect and study all activity
    # make bot stuff as soon as possible to show them hey this is working till tommoreoow figure what we going to demo them on 15
    # run diff ip on instagram
    # make at least 10 fake user
    # put 10 fake user name and try to use ip they provided
chrome_options.add_argument(PROXY1)
chrome_options.add_argument('--proxy-server=%s' % PROXY1)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://127.0.0.1/pcrecords/index.php")

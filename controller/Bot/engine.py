from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import MySQLdb
import requests
from flaskext.mysql import MySQL
# from init import botstart
from selenium import webdriver
from instagram.client import InstagramAPI
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time,sched

s = sched.scheduler(time.time, time.sleep)


PROXY = "127.0.0.1" # IP:PORT or HOST:PORT
PROXY1 = "127.0.0.1:34002" # IP:PORT or HOST:PORT
PROXY2 = "127.0.0.1:34003" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
#
# opener = urllib.request.build_opener(
#                                      urllib.request.ProxyHandler(
#                                                                  {'https':'https://127.0.0.1:34004'}))
# chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
#
# chrome = webdriver.Chrome(chrome_options=chrome_options)
# getdriver =("http://whatismyipaddress.com")
# chrome.get("http://whatismyipaddress.com")
# driver = webdriver.Chrome()
# driver.get(getdriver)
# driver.get(getdriver)
#

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'canam1234'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
username = "jeffrr111111"
password = "jeff1234"
target='gagan_babrah_7860'
target1='jeffrr111111'
# time.sleep(3)




    # driver1.find_element_by_xpath("//input[@name='username']").send_keys(username)
    # driver1.find_element_by_xpath("//input[@name='password']").send_keys(password)
    # driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    # time.sleep(3)
    # i=0
    #
    # # "x%d"%i = data[:,i-1]
    #
    #
    # r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
    # driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
#     # wait = WebDriverWait(driver, 20)
#     # driver1.find_element_linktext('/navjotbabrah/').click()
# time.sleep(4)
# dd1 = ("https://www.instagram.com/navbabrah/")
# driver1 = chrome
# driver1.get(dd1)
# driver1.find_element_by_css_selector('._phrgb').click()
# time.sleep(4)
# print(driver1.get('https://lumtest.com/myip.json'))
# i+=1
# wait = WebDriverWait(driver1, 10)
# langselction = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "_phrgb")))
# langselction.click()
# driver1.find_element_by_css_selector('._q6fzq').click()
    #////////////////////////////////////////////
    # # driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
    # time.sleep(4)
    # age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._oluat")))
    # age.click()
    # time.sleep(4)
    # age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._phrgb")))
    # age1.click()
    # print(driver1.get('https://lumtest.com/myip.json'))
    # s.enter(30, 1, doo_something, (sc,))

# s.enter(30, 1, doo_something, (s,))
# s.run()

	#
	# page = requests.get("http://google.com")
	# page.status_code
	# soup = BeautifulSoup(page.content, 'html.parser')
	# soup.find_all(id="lga")


@app.route('/signin')
def index1():
	 if request.method == 'GET':
		 return render_template('public/signin.html')
@app.route('/admin')
def admin():
	 if request.method == 'GET':
		 return render_template('admin_boostlikes/index.html')
	#admin
	#admin

@app.route('/signup')
def index2():
	 if request.method == 'GET':
		 return render_template('public/signup.html')
	#

@app.route('/home')
def index3():
	 if request.method == 'GET':
		 return render_template('adminml/home.html')
	#
@app.route('/follow',methods=['POST','GET'])
def follow():
    if request.method == 'POST':
        params = request.form
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY2)
        chrome = webdriver.Chrome(chrome_options=chrome_options)

        dd1 = ("https://www.instagram.com/accounts/login/")
        driver1 = chrome
        driver1.get(dd1)
        driver1.find_element_by_xpath("//input[@name='username']").send_keys(username)
        driver1.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
        time.sleep(3)
        i=0

            # "x%d"%i = data[:,i-1]


        r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
            # driver1.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target1)

        d=0
        target=['luxury.lifes']

        for i in target:
            if (d!=len(target)):
                url=  ("https://www.instagram.com/"+ "".join(str(i)))

                dd1 = url
                driver1 = chrome
                driver1.get(dd1)
                time.sleep(5)
                driver1.find_element_by_css_selector('._phrgb').click()

        # driver1.find_element_by_css_selector('._soakw ._vbtk2 ').click()
                print(driver1.get('https://lumtest.com/myip.json'))
                d+1




    	return render_template('admin_boostlikes/autoround.html')




@app.route('/autolike')
def index4():
	 if request.method == 'GET':
		 return render_template('admin_boostlikes/index.html')
	#

@app.route('/dashboard')
def index5():

	 if request.method == 'GET':
		 return render_template('admin_boostlikes/index.html')
	#

@app.route('/AutoRound',methods=['POST','GET'])
def index6():
    if request.method == 'GET':
        return render_template('admin_boostlikes/autoround.html')

    if request.method == 'POST':
        params = request.form

        chrome_options.add_argument('--proxy-server=http://%s' % PROXY1)

        chrome = webdriver.Chrome(chrome_options=chrome_options)

        dd1 = ("https://www.instagram.com/accounts/login/")
        driver1 = chrome
        driver1.get(dd1)
        driver1.find_element_by_xpath("//input[@name='username']").send_keys(username)
        driver1.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver1.find_element_by_xpath("//button[contains(.,'Log in')]").click()
        time.sleep(3)
        i=0

        # "x%d"%i = data[:,i-1]


        r=driver1.find_element_by_xpath("//div[@class='_a1rcs']").click()
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
                driver1.find_element_by_css_selector('._tk4ba').click()
            # driver1.find_element_by_css_selector('._phrgb').click() for follow
                time.sleep(4)
                driver1.find_element_by_css_selector('._3eajp').click()
                time.sleep(4)

        # driver1.find_element_by_css_selector('._soakw ._vbtk2 ').click()
                print(driver1.get('https://lumtest.com/myip.json'))
                d+1




	return render_template('admin_boostlikes/autoround.html')

	#  if request.method == 'POST':
     #
     #
	# 	 return render_template('admin_boostlikes/autoround.html')
	# 	 #

		# params = request.form
		# print params
		# round1 = params['round1']
		# round2 = params['round2']
		# round3 = params['name']
		# account = params['account']
		# username = params['username']
		# resume = request.files['resume']
		# resume.name = resume.filename5
	#

#
# @app.route('/',methods=['POST','GET'])
# def user_auth():
# 	print 'this runs after request'
#         ctx = app.test_request_context()
#         ctx.push()
#         ctx.pop()
#         app.config['MYSQL_DATABASE_USER'] = 'root'
#         app.config['MYSQL_DATABASE_PASSWORD'] = 'canam1234'
#
#         app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("USE Boostlikes;")
#
#         rv2 = request.form.get('username',type=str)
#         rv1 = request.form.get('password',type=str)
#         print rv2
#         print rv1
#         print rv3
#         cursor.execute("INSERT INTO `user-assigned`( `username`, `password`) VALUES ( %s, %s)", (request.form.get('username'), request.form.get('password')))
#
#

if __name__ == '__main__':
	app.run(host ='0.0.0.0',port=8621,debug=True,threaded=True)

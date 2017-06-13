from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import MySQLdb
import requests,urllib
from flaskext.mysql import MySQL
# from init import botstart
import engine
mysql = MySQL()
app = Flask(__name__,static_folder='static', static_url_path='/static')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'canam1234'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index():
	#
	# page = requests.get("http://google.com")
	# page.status_code
	# soup = BeautifulSoup(page.content, 'html.parser')
	# soup.find_all(id="lga")

	return render_template('public/index.php')
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
def indexhome():
	 if request.method == 'GET':
		 return render_template('adminm/home.html')
	#
@app.route('/about')
def indexabout():
	 if request.method == 'GET':
		 return render_template('public/about.html')

@app.route('/Boost')
def index3():
	 if request.method == 'GET':
		 return render_template('admin_boostlikes/Boost.html')
@app.route('/Listlike')
def index4():
	 if request.method == 'GET':
		 return render_template('admin_boostlikes/Listlike.html')
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
		#  engine.index6()
		 return render_template('admin_boostlikes/autoround.html')
		#  engine.index()
	#  if request.method == 'POST':
	# 	#  engine.index()

	#  if request.method == 'POST':
	#
	 #
	# 	 return render_template('admin_boostlikes/autoround.html')
		 #

		# params = request.form
		# print params
		# round1 = params['round1']
		# round2 = params['round2']
		# round3 = params['name']
		# account = params['account']
		# username = params['username']
		# resume = request.files['resume']
		# resume.name = resume.filename

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




if __name__ == '__main__':
	app.run(host ='0.0.0.0',port=8131,debug=True,threaded=True)

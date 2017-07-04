import sys
import logging
#from main import app as application
#activate_this = '/var/www/html/boost/boost/env/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))
 #project_home = '/opt/appdir/Application/myapp'
 #project_web  = '/opt/appdir/Application/myapp/web'


logging.basicConfig(stream=sys.stderr)
f = '/var/www/html/boost'
if not f in sys.path:
    sys.path.insert(0, f)

#from main import app as application
from main import app
application = app

#application.secret_key = '3121231232123edqeqwe213`@!@!'

#if __name__ == "__main__":
 #   app.run()













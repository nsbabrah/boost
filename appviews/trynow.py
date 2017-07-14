from flask import request,render_template
from approutes import my_view

@my_view.route ('/trynow')
def trynow():
    if request.method == 'GET':
        return render_template ('public/trynow.html')
        #
from approutes import my_view

from flask import redirect,request,url_for
from flask_login import logout_user,login_required

@my_view.route ("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('my_view.verify_user_password'))


from approutes import my_view

from controller.Bot import lumi
@my_view.route('/startlistlike',methods=['POST'])
def startlistlikes():


    lumi.userprofile_start(user,listlikes,accname)

    return 'START'




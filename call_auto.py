# # # # from lumi import userprofile_info
# # # import time,sched
# # # import threading
# # # from threading import Thread
# # # import time
# # # from selenium import webdriver
# # # from instagram.client import InstagramAPI
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from selenium.webdriver.common.keys import Keys
# # # import time,sched
# # # import sched
# # #
# # #
# # # s = sched.scheduler(time.time, time.sleep)
# # #
# # #
# # #
# # # d=['1',
# # # '2']
# # #
# # # import time
# # # from threading import Timer
# # # chrome_options = webdriver.ChromeOptions()
# # # chrome_options.add_argument('--proxy-server=http://%s' % '127.0.0.1:34002')
# # #
# # #
# # # browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")
# # # browser.get('http:/reddit.com')
# # # d=webdriver.Chrome(chrome_options=chrome_options,executable_path=r"../../Downloads/chromedriver")
# # # d.get('https://www.
# # # babrah.com')
# # #
# # # # def Auto_gen1(sc):
# # # #     d=0
# # # #     for _ in range(3):
# # # #         userprofile_info()
# # # #         userprofile_info()
# # # #         userprofile_info()
# # # #         userprofile_info()
# # # #
# # # # repeat_fun(3, Auto_gen1)
# # # #     # Auto_gen1()s
# # # # #
# # # # # def print_time():
# # # # #     userprofile_info()
# # # # #     # print "From print_time", time.time()
# # # # # def print_time1():
# # # # #     userprofile_info()
# # # # #     # print "Fro
# # # # # def print_some_times():
# # # # #     # print time.time()
# # # # #     Timer(5, print_time(),print_time1()).start()
# # # # #     if(d==1):
# # # # #         Timer(5.1, print_time, ()).start()
# # # # #         print 'second'
# # # # #     # time.sleep(11)  # sleep while time-delay events execute
# # # # #         # print time.time()
# # # # # print_some_times()
# # # from multiprocessing import Process
# # # import sys
# # # # import lumi
# # # from crontab import CronTab
# # # # my_cron = CronTab(user='ss')
# # #
# # # # empty_cron = CronTab()
# # # # my_cron = CronTab(user=True)
# # # # users_cron = CronTab(user='username')
# # # # my_cron = CronTab()
# # #
# # # rocket = 0
# # # # file_cron = CronTab(tabfile='filename.tab')
# # # my_cron = CronTab(user='your username')
# # # job = my_cron.new(command='python lumi.py')
# # # job.minute.every(1)
# #
# # import threading
# # # import lumi
# # # thr = [threading.Thread(target=userprofile_info, args=(), kwargs={})for _i in range(5)]
# # # thr.start(1) # will run "foo"
# # # # ....
# # # thr.is_alive(4) # will return whether foo is running currently
# # # # ....
# # # thr.join(1) # will wait till "foo" is done
# # # print 'hrll'
# # # # my_cron.start()
# # # job = CronTab(command='python /home/roy/writeDate.py')
# # # # my_cron.minute.every(1)
# # def main():
# #     from crontab import CronTab
# #
# #     cron = CronTab(user='kk')
# #
# #     job = cron.new(command='python lumi.py')
# #     job.minute.on(0.5)
# #     # job.hour.on(12)
# #
# #     cron.write()
# #
# # if __name__ == "__main__":
# #   main()
# import gevent.monkey
# from urllib.request import urlopen
# gevent.monkey.patch_all()
# urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']
#
# def print_head(url):
#     print('Starting {}'.format(url))
#     data = urlopen(url).read()
#     print('{}: {} bytes: {}'.format(url, len(data), data))
#
# jobs = [gevent.spawn(print_head, _url) for _url in urls]
#
# gevent.wait(jobs)
# # # my_cron.write()
# #
# # # def func1():
# # #     global rocket
# # #     print 'start func1'
# # #     while rocket < sys.maxsize:
# # #         rocket += 1
# # #         userprofile_info()
# # #
# # #
# # #     print 'end func1'
# # #
# # # def func2():
# # #     global rocket
# # #     print 'start func2'
# # #     while rocket < sys.maxsize:
# # #         rocket += 1
# # #         userprofile_info1()
# # #     print 'end func2'
# #
# #     #  p1 = Process(target = func1)
# #     #  p1.start()
# #     #  p2 = Process(target = func2)
# #     #  p2.start()
from crontab import CronTab

# system_cron = CronTab()
# user_cron = CronTab('root')
# file_cron = CronTab(tabfile='filename.tab')
# mem_cron = CronTab(tab="""
#   * * * * * command
# """)
def my_cron_job1():
    print "cron job 1"

def my_cron_job2():
    print "cron job 2"

def my_interval_job():
    print "interval job"

if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler(timezone='MST')

    sched.add_job(my_interval_job, 'interval', id='my_job_id', seconds=5)

    sched.add_job(my_cron_job1, 'cron', id='my_cron_job1', minute=10)
    sched.add_job(my_cron_job2, 'cron', id='my_cron_job2', minute=20)
from multiprocessing import Process, Queue
# import lumi
import types
from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print "Hello World"

sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

sched.start()

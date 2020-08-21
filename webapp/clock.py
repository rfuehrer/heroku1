#! /usr/bin/env python3
#import os
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every one minutes.')
#    os.spawnl(os.P_NOWAIT, '/opt/webapp/folding-stats.py')
    pid = subprocess.Popen(["python3", "/opt/webapp/folding-stats.py"], creationflags=subprocess.DETACHED_PROCESS)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
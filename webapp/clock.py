#! /usr/bin/env python3
#import os
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every one minutes.')
#    os.spawnl(os.P_NOWAIT, '/opt/webapp/folding-stats.py')
    cmd = "python3 /opt/webapp/folding-stats.py"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
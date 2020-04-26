from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from good_morning import sendmorningmessage



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(sendmorningmessage, 'interval', seconds=2)

sched.start()
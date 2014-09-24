from pytz import utc
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
# import subprocess



def my_job():
    print "HELLLLOOO WORLD"
    # subprocess.Popen("make-call.py", shell=True)

if __name__ == '__main__':
  sched = BlockingScheduler()
  sched.configure(timezone=utc)
  sched.add_job(my_job, 'date', run_date=datetime(2014, 9, 24, 12, 47,0))
  try:
      sched.start()
  except (KeyboardInterrupt, SystemExit):
      pass
  scheduler.shutdown()
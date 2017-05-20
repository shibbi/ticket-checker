import scraper

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

def job():
  scraper.Scraper()

sched = BlockingScheduler()
sched.add_job(job, 'cron', minute=1, id='scraper', name='Scrape tickets every hour')
sched.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

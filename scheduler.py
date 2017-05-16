import scraper

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

def job():
  print('This scraper is run every 10 minutes.')
  scraper.Scraper()

sched.add_job(job, 'interval', minutes=10)

sched.start()

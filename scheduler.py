import scraper

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(scraper.Scraper, 'interval', minutes=60)

import re, urlparse
from datetime import datetime

from selenium import webdriver
from bs4 import BeautifulSoup

class Scraper(object):
  def __init__(self):
    link = 'https://www1.ticketmaster.com/2018-monsta-x-us-tour-sugar-land-texas-07-29-2018/event/3A0054496F601C07'

    # initialize phantomJS driver
    self.driver = webdriver.PhantomJS()
    self.driver.set_window_size(1120, 550)

    # go to the page
    self.driver.get(link)

    # parse the page and find all buttons with class
    soup = BeautifulSoup(self.driver.page_source, "html.parser")
    buttons = soup.find_all('button', { 'class': 'rc-slider__label-button' })

    # look for the last button and print the text
    # if not found print all the buttons
    last_button = None
    for last_button in buttons:pass
    if last_button:
      print "highest price at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + last_button.getText()
    else:
      print "no tickets found"

    self.driver.quit()

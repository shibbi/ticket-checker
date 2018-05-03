import re, urlparse
from datetime import datetime

from selenium import webdriver
from bs4 import BeautifulSoup

class Scraper(object):
  def find(self, event, link):
    # go to the page
    self.driver.get(link)

    # parse the page and find all buttons with class
    soup = BeautifulSoup(self.driver.page_source, "html.parser")
    buttons = soup.find_all('button', { 'class': 'rc-slider__label-button' })

    # look for the last button and print the text
    # if not found print all the buttons
    last_button = None
    for last_button in buttons:pass
    print event + ": "
    if last_button:
      print "highest price at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + last_button.getText()
    else:
      print "no tickets found"

  def __init__(self):
    # initialize phantomJS driver
    self.driver = webdriver.PhantomJS()
    self.driver.set_window_size(1120, 550)
    
    event = "got7 hou"
    link = 'https://www1.ticketmaster.com/event/3A005490FB58A38E'
    self.find(event, link)

    event = "got7 la"
    link = 'https://www1.ticketmaster.com/event/0900549215DC6833'
    self.find(event, link)

    self.driver.quit()
  
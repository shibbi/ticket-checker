import re, urlparse

from selenium import webdriver
from bs4 import BeautifulSoup

class Scraper(object):
  def __init__(self):
    link = 'https://www1.ticketmaster.com/kcon-2017-ny-presented-by-toyota-newark-new-jersey/event/020052A2A7C972E2'

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
      print last_button.getText()
    else:
      print buttons

    self.driver.quit()
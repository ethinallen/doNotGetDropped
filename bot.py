import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class bot():

    def __init__(self):
        # load credentials to log into the textbook
        self.credentials, self.paths = self.loadCredentials()

        # make a driver instance to get to the textbook
        self.driver = self.makeDriver()

        # url of the textbook
        url = 'https://newconnect.mheducation.com/flow/connect.html'

        # navigate to the textbook
        self.navigate(self.driver, url)

        time.sleep(15)

        # login to textbook
        self.login(self.driver, self.credentials, self.paths)

    def loadCredentials(self):

        # load login credentials for mcgraw hill connect
        with open('credentials.json') as f:
            credentials = json.load(f)

        # load the paths to buttons whose locations we need
        with open('paths.json') as f:
            paths = json.load(f)

        return credentials, paths

    # make a driver
    def makeDriver(self):
        driver = webdriver.Firefox()
        return driver

    # navigate driver to a page
    def navigate(self, driver, destination):
        self.driver.get(destination)

    def login(self, driver, credentials, paths):

        # load all of our paths
        userPath = paths['username']
        pwPath = paths['password']
        submitButton = paths['submit']

        # get individual credentials
        user = credentials['username']
        pw = credentials['password']

        driver.implicitly_wait(20)

        # send username and password
        sendPW = driver.find_element_by_css_selector('#ember575')
        # sendPW.sendKeys(user)
        print(sendPW)

    def getVideos():
        yield None

if __name__ == '__main__':
    bot = bot()

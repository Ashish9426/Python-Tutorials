# import selenium for communicating with web driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def function1():
    # open the Chrome browser using chrome driver
    browser = webdriver.Chrome(executable_path='/Users/amitk/selenium/chromedriver')

    # visit the google url
    browser.get('https://google.co.in')

    # find the input having name = q
    input = browser.find_element_by_name('q')

    # enter the search text
    input.send_keys("iPhone 12")

    # press enter
    input.send_keys(Keys.ENTER)

    # sleep for 5 seconds
    time.sleep(3)

    # close the browser
    browser.close()


function1()
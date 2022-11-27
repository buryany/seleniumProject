# Chapter 4:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

HOST = "https://demoqa.com/browser-windows"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)

try:
    print("Starting test with various locator to use in find_element() method.")
    driver.get(HOST)
    # time.sleep(5)
    #enter first_name = 'john', enter last_name = 'doe', enter email = 'jdoe@email.com',
    # select radio button gender = 'male',
    # date of birth = 27 November 2000, subject = 'selenium forms testing'
    #select checkboxes, select Sports, reading, music
    #upload picture
    #enter massage in the text_area = '2906 Shell Rd., Brooklyn NY 12224'
    # check is the city is enabled
    #select state = 'NCR'
    #select city = 'Delhi'
    #check if male gender is selected
    #check if sports hobbies is selected
    #click submit
    #verify the massage:





except Exception as err:
    print("Python Exception: test failed with following exception.")
    print(err)
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    # pass


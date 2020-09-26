import json
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
from os import path
import csv

def getChromeDriver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    return webdriver.Chrome(options=options)

if  __name__ == "__main__":
    driver = getChromeDriver()
    driver.get("http://www.gmatfree.com/module-2/buses-passengers-and-folders/?explanation=1")
    driver.implicitly_wait(10)
    time.sleep(5)
    element = driver.find_element_by_css_selector("#question_5610_multi_5612_ans_3")
    element.click()
    time.sleep(10)
    driver.close()

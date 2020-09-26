import json
from time import gmtime, strftime
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# import requests
# import urllib.request
from os import path
import os, uuid
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# import pyodbc
# from PIL import Image
# from fake_useragent import UserAgent
script_path = os.getcwd()

# def get_header() :
#     ua=UserAgent()
#     return {'User-Agent': ua.random,       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',      'Accept-Encoding': 'none',      'Accept-Language': 'en-US,en;q=0.8',      'Connection': 'keep-alive'}

def getChromeDriver():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    # options.add_argument("download.default_directory=C:/Downloads")
    # prefs = {'download.default_directory' : 'path/to/dir'}
    # options.add_experimental_option('prefs', prefs)
    # chromedriver = 'DESCTINATION_TO_YOUR_CHROME_DRIVER'
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver_path=script_path + '/chromedriver'
    driver_path= path.expanduser("~") + '/AppData/Local/Google/Chrome/User Data'
    print(driver_path)
    options.add_argument('--user-data-dir=' + path.expanduser("~") + '/AppData/Local/Google/Chrome/User Data')
    # return webdriver.Chrome(options=options, executable_path=driver_path)
    return webdriver.Chrome(options=options)

if  __name__ == "__main__":
    
    driver = getChromeDriver()
    driver.implicitly_wait(10)
    driver.get("https://wwwsc.ekeystone.com/")



    # driver.close()

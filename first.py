from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


import time
import chromedriver_binary


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--test-type")
# chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)
# url = "http://www.gmatfree.com/module-2/buses-passengers-and-folders/?explanation=1"
# driver.get(url)
driver.get('https://wikipedia.com')

search_language = driver.find_element_by_id('searchLanguage')
search_language.text

f = open("demo.txt", "w")
f.write(search_language.text)
f.close()

# Select(search_language).select_by_visible_text('Latina')

# search_textinput = driver.find_element_by_id('searchInput')
# search_textinput.send_keys('Marcus Aurelius')

# search_button = driver.find_element_by_xpath(
# '/html/body/div[2]/form/fieldset/button/i'
# )



driver.quit()
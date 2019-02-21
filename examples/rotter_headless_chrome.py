import os  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  

CHROMEDRIVER_PATH = '/Users/ynonperek/bin/chromedriver'

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

# Start Here
driver.get("http://rotter.net/")
news = driver.find_elements_by_css_selector('a[target="news"] span')
for item in news:
    print(item.text)

driver.close()


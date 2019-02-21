import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

CHROMEDRIVER_PATH = '/Users/ynonperek/bin/chromedriver'

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

# Start Here
driver.get("https://www.ynet.co.il/home/0,7340,L-184,00.html")
news = driver.find_elements_by_css_selector('a.smallheader')
for item in news:
    print(item.text)

driver.close()



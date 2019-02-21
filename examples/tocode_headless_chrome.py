import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(executable_path=os.path.abspath("/Users/ynonperek/bin/chromedriver"), chrome_options=chrome_options)  
driver.get("https://www.tocode.co.il")

print(driver.title)

driver.close()

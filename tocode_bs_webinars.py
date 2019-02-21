import requests
from bs4 import BeautifulSoup

url = 'https://www.tocode.co.il/workshops'
r = requests.get(url)
soup = BeautifulSoup(r.text)

for link in soup.select('.workshopHeader'):
    print(link.text)

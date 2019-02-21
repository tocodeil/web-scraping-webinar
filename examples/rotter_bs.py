import requests
from bs4 import BeautifulSoup
import pdb

url = 'http://rotter.net/'
r = requests.get(url)
r.encoding = 'iso8859-8'
soup = BeautifulSoup(r.text,  'html5lib')
for link in soup.select('[target="news"] > span'):
    print(link.text)

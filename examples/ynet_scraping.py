import requests
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession
import collections

url = 'https://www.ynet.co.il/home/0,7340,L-184,00.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')

urls = [f'https://www.ynet.co.il{item.get("href")}' for item in soup.select('a.smallheader')]

# print(urls)

word_counter = collections.Counter()

def parse_ynet_article(resp, *args, **kwargs):
    page = BeautifulSoup(resp.text, 'html5lib')
    text = page.select('.art_body span')[0].text
    word_counter.update(text.split())

session = FuturesSession()
session.hooks['response'] = parse_ynet_article

q = [session.get(url) for url in urls]
results = [f.result() for f in q]
print(len(results))
print(word_counter)

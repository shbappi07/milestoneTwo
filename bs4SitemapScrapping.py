import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.discovermagazine.com/sitemap/article/environment/1.xml'

r = requests.get(url)
data = r.text

soup = bs(data, 'html.parser')
locs = soup.findAll('loc')
for loc in locs:
    print(loc.text)

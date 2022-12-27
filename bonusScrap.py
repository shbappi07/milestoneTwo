import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data,'html.parser')
h1 = soup.find('h1')
print(h1.text)

link = soup.find('a')
print(link.text)

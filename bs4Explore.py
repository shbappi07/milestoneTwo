import requests
from bs4 import BeautifulSoup

url ='https://quotes.toscrape.com'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

links = soup.findAll('a')
for link in links:
    all_links = f'{url}'+link.get('href')
    print(all_links)


import httpx
from pprint import pprint

key_wrod = input('Enter your query: ')
def slug(key):
    if ' ' in key:
        url_slug = key.replace(' ', '+')
        return url_slug
# print(slug(key_wrod))

api_url = f'https://pixabay.com/api/?key=11017218-149c81a9dfc78599195fc18d3&q={slug(key_wrod)}&image_type=photo'
# print(api_url)

r = httpx.get(api_url)
data = r.json()

image_match = data.get('total')
# print('Total match: ',image_match)

if image_match >0:
    print('Total Match: ',image_match)
    hits = data.get('hits')
    for hit in hits:
        # image_id = hit.get('id')
        # print(image_id)
        webformatURL= hit.get('webformatURL')
        print(webformatURL)
else:
    print('No image found')

# pprint(hits)
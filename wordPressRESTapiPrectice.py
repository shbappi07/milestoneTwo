import pprint
import httpx

site_url = 'https://varcampus.com/wp-json/wp/v2'

post_url = f'{site_url}/posts'

r = httpx.get(post_url)
datas = r.json()
for data in datas:
    urls = data.get('link')
    title = data.get('title').get('rendered')
    print(urls,title)

    
# pprint.pprint(r.json())
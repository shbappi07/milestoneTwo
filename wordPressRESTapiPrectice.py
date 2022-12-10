import pprint
import httpx

site_url = 'https://varcampus.com/wp-json/wp/v2'

post_url = f'{site_url}/posts'

r = httpx.get(post_url)
datas = r.json()
for data in datas:
    urls = data.get('link')
    title = data.get('title').get('rendered')
    statuses = data.get('status')
    # print('status: ',statuses,'url: ',urls,'Title:',title)

    #write to local file
    text = f'{statuses}:\n{urls}\n\nTitle: {title}\n\n'
    file = open('urls dara.txt','a+')
    file.writelines(text+'\n')
    file.close()
    print('success')



import httpx
file = open('pixabayUrls.txt','r+')
url_lists=file.readlines()
file.close()

# print(url_lists)

new_url_lists = []

for url in url_lists:
    fresh_url = url.rstrip('\n')
    new_url_lists.append(fresh_url)

# print(new_url_lists)

# single image download
count = 0
for single_url in new_url_lists:
# single_url = new_url_lists[0]
    r = httpx.get(single_url)
    with open(f'images/rose{count}.jpg', 'wb+') as file:
        file.write(r.content)
        print('success')
    count += 1
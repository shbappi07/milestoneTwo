import httpx

url_lists = [
    'https://www.upwork.com/services/product/marketing-100k-telegram-member-for-your-crypto-community-1445489760877760512?ref=project_share',
    'https://www.youtube.com/watch?v=4EfQ2WtxyLw',
    'https://www.weatherapi.com/my/',
    'https://www.varcampus.com'
]

for url_list in url_lists:
    status = httpx.get(url_list).status_code
    print(status, 'url- ',url_list)

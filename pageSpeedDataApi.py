import requests
url = input('Enter your test url: ')
api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}'

response_data = requests.get(api_url)
data = response_data.json()

if response_data.status_code == 200:
    originLoadingExperience = data.get('loadingExperience').get('metrics').get('CUMULATIVE_LAYOUT_SHIFT_SCORE').get('percentile')
else:
    print('something wrong')

# print(originLoadingExperience)
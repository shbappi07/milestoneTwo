import httpx
import base64
import pprint
rest_contry_api = 'https://restcountries.com/v3.1/all'
r = httpx.get(rest_contry_api).json()

countries = []
for country in r:
    name = country.get('name').get('common')
    # official_name = country.get('name').get('official')
    countries.append(name)
# print(countries)

wp_user = 'shbappi07'
wp_pass = 'Nme3 8kLk jKuQ cNUn 1KTF 1I1d'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

post_url = 'https://localhost/mobile/wp-json/wp/v2/categories'
post_data = {
    'name':f'{countries}',
    # 'slug':f'{official_name}'
}

res = httpx.post(post_url,data=post_data,headers=wp_header,verify=False)
print(res.status_code)
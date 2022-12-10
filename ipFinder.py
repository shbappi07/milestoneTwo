import requests

url = 'https://api.ipify.org?format=json'

ip_response = requests.get(url).json()
ip = ip_response.get('ip')
# print(ip)


# ip details finder

ip_detais_url =f'https://ipapi.co/{ip}/json/'

res_details = requests.get(ip_detais_url).json()

city = res_details.get('city')
region = res_details.get('region')
country = res_details.get('country_name')
time_zone = res_details.get('utc_offset')
population = res_details.get('country_population')
sentence = f'You are looking for the ip address {ip}. This ip address is in {city},{region}. The origin of this ip is {country}. It is in {time_zone} time zone. Total population in {country} is {population}'
# print(res_details)
print(sentence)
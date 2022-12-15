import base64
import httpx

wp_user = 'shbappi07'
wp_pass = 'Nme3 8kLk jKuQ cNUn 1KTF 1I1d'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())

wp_header = {'Authorization':f'Basic {wp_token.decode("utf-8")}'}

post_url = 'https://localhost/mobile/wp-json/wp/v2/posts'
post_data = {
    'title':'This is an awesome title post',
    'slug':'This is an awesome slug',
    'status':'publish',
    'content':'This is an awesome content for awesome post',
    'categories':'4'
}

r = httpx.post(post_url,data=post_data,headers=wp_header,verify=False)
print(r.status_code)
print(r.json())
import base64
import httpx

wp_user = 'shbappi07'
wp_pass = 'Nme3 8kLk jKuQ cNUn 1KTF 1I1d'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())

wp_header = {'Authorization':f'Basic {wp_token.decode("utf-8")}'}

title = 'this is the complete wordpress post title'
paragraph = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)'

post_data = {
    'title':title,
    'slug':'This is complete wordpress posting',
    'content':paragraph,
    'categories':'4'
}
post_url = 'https://localhost/mobile/wp-json/wp/v2/posts'
r = httpx.post(post_url,data=post_data,headers=wp_header,verify=False)
print(r.status_code)
print(r.json())
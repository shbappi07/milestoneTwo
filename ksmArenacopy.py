import json

import httpx
from pprint import pprint
api_url = 'https://mobile-phone-server.vercel.app/phones'

r = httpx.get(api_url)
data = r.json()

get_records = data.get('RECORDS')

def wp_feature_image(img_src,phone_name):
    code = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --><figure class="wp-block-image aligncenter size-large"><img src="{img_src}" alt="{phone_name} image"/><figcaption class="wp-element-caption">{phone_name}</figcaption></figure><!-- /wp:image -->'
    return code
def wp_dictionary_table(dictionary):
    code = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        code += tr_data
    code += '</tbody></table></figure><!-- /wp:table -->'
    return code

def wp_paragraph(text):
    content = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return content

def wp_heading_two(text):
    return f'<!-- wp:heading --><h2>{text} Overview</h2><!-- /wp:heading -->'

def concatenate_string(*args):
    final = ''
    for arg in args:
        final += arg
    return final


for phone in get_records:
    name = phone.get('name')
    release_date = phone.get('released_at')
    body = phone.get('body')
    chipset = phone.get('chipset')
    os = phone.get('os')
    ram = phone.get('ram')
    storage = phone.get('storage')
    camera_pixels = phone.get('camera_pixels')
    picture = phone.get('picture')

    ov_dictionary = {
        'name': name,
        'release date': release_date,
        'body': body,
        'chipset': chipset,
        'os': os,
        'ram': ram,
        'storage': storage,
        'camera': camera_pixels,

    }

    intro_paragraph = f'{name} has been {release_date}. It comes with {chipset}. The body of this mobile is {body}. {os} is the built in android version. {name} has {ram} and has {storage} with the camera resolution of {camera_pixels}'
    main_para = wp_paragraph(intro_paragraph)
    main_img = wp_feature_image(picture,name)
    h2 = wp_heading_two(name)
    overview_table = wp_dictionary_table(ov_dictionary)

    # print(main_para, main_img, h2, overview_table)
    second_heading = wp_heading_two(f'{name} specifications')
    specifications_data = phone.get('specifications')
    specifications = json.loads(specifications_data)
    specification_table = wp_dictionary_table(specifications)

    content = concatenate_string(main_para,main_img,h2,overview_table,second_heading,specification_table)
    print(content)

# start from 114

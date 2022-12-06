mobile_data = [
    {'name':'xiomi','price':3030, 'ram':'8gb'},
    ['doel','koyel','syama'],
    {'name':'samsung','price':34400, 'ram':'10gb'},
    {'name':'apple','price':334500, 'ram':'11gb'}
]
for data in mobile_data:
    try:
       print(f'{data.get("name")} is a very well known brand in the world. The new price of name is {data.get("price")} with {data.get("ram")} ram.')
    except:
        # print('error')
        pass
import requests 


responce = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95&page=2&sort=sale/dc')
data = responce.json()
for product in data['prods']:
    name = product['name']
    price = product['price']
    print(name)
    print(price)
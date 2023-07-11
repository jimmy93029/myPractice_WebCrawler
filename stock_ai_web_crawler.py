import requests
from bs4 import BeautifulSoup
from pprint import pprint

r = requests.get('https://chart.stock-ai.com/history?symbol=AAPL&resolution=D&from=1658843877&to=1659707877')
if r.status_code == requests.codes.ok:
    data = r.json()
    zipped = zip(data['o'],data['h'],data['l'],data['c'],data['v'])
    pprint(list(zipped))
else:
    print('requests code is not ok')


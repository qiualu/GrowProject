import requests
from lxml import etree


url = 'http://quote.eastmoney.com/stocklist.html'

response = requests.get(url)
print(response)
a = ''
for e in response:
    a = a + e

print(a)
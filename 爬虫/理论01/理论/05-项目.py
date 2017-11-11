import requests
from lxml import etree

header = {
    'CONNECT clients2.google.com':'443 HTTP/1.1',
    'Host': 'clients2.google.com:443',
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
def printEleListTxt(elelist):
	for e in elelist :
		print('text = ' + e.text)
# response = requests.get('http://www.qianmu.org/%E5%93%88%E4%BD%9B%E5%A4%A7%E5%AD%A6',headers=header)
# print(response)

#世界大学排名
# http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D
response = requests.get('http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D',headers=header)
html = etree.HTML(response.text)

学校名 = html.xpath('//*[@id="content"]/table/tbody/tr/td[2]/text() | //*[@id="content"]/table/tbody/tr/td[2]/a/text()')
print(学校名)
print(len(学校名))

path = 'D:\Project\爬虫\理论01\学校名.txt'
with open(path,'a+') as f:
    f.write(str(str(学校名).encode('gbk')))



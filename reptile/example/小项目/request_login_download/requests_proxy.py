# coding=utf-8

import requests
from lxml import etree
import random

headers_1 = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

# https ip 集合
https_ip = [
'180.173.70.40:9797',
'183.15.27.168:9999',
]

# http ip 集合
http_ip = [
'125.46.0.62:53281',
'118.119.168.172:9999',
]

# 从集合中随机选择代理ip进行设置
proxy_ip = {
'https':random.choice(https_ip),
'http':random.choice(http_ip),
}

print(proxy_ip)

# 使用代理 ip 发送请求
response = requests.get('http://ip.filefab.com/index.php',
                        proxies = proxy_ip)

html = etree.HTML(response.text)

ip = html.xpath("//h1[@id='ipd']/span/text()")

print(ip)





#coding=utf-8
import requests
from lxml import etree
headers_1 = {
# 'Upgrade-Insecure-Requests':'1',
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer':'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
}

# proxies
proxy_ip = {
    'http':'58.251.248.251:8118'
}
response = requests.get('http://ip.filefab.com/index.php',
                        headers = headers_1,
                        proxies = proxy_ip
                         )
html = etree.HTML(response.text)
ip = html.xpath('//*[@id="ipd"]/span/text()')
print(ip)
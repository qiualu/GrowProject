#coding=utf-8
import requests

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}

response = requests.get('http://www.baidu.com',headers = header)

print(response.url)
print(response.headers)
for e in response.headers:
    print(e," : ",response.headers[e])



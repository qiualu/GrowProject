# coding=utf-8

import requests
import time

headers_1 = {
'Upgrade-Insecure-Requests':'1',
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer':'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
}
headers_2 = {
'from':'http://so.gushiwen.org/user/collect.aspx',
'__VIEWSTATE':'tj1kA2Nwo2PGYTwOvlI08eeEyWde9Rnx3BTQjBmaseKfjsuqlPEiTIrnGLUaV6eVnM92tyQJawWwIoirjMu1UuoVMOLakUb+F/Kv/DCYCh8pUTpyQHfoPvmfbhY=',
'__VIEWSTATEGENERATOR':'C93BE1AE',
'email':'1090509990@qq.com',
'pwd':'123456',
'code':'plwt',
'denglu':'登录',
}


# 生成 session 对象
sess = requests.session()

response = sess.get('http://so.gushiwen.org/user/collect.aspx', headers=headers_2)

print(response.text)




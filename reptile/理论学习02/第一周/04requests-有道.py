# coding=utf-8

import requests

# 生成 session 对象
sess = requests.session()

# 使用 session 对象 访问首页
# 目的获取 cookies
# print( { e.name:e.value for e in sess.cookies} )
sess.get('http://fanyi.youdao.com/')
print( { e.name:e.value for e in sess.cookies} )

headers_base = {
'Host':' fanyi.youdao.com',
'Connection':' keep-alive',
'Content-Length':' 218',
'Accept':' application/json, text/javascript, */*; q=0.01',
'Origin':' http://fanyi.youdao.com',
'X-Requested-With':' XMLHttpRequest',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'Referer':' http://fanyi.youdao.com/',
'Accept-Encoding':' gzip, deflate',
'Accept-Language':' zh-CN,zh;q=0.8',
}

tran_data = {
# 'smartresult':'dict',
# 'smartresult':'rule',
# 'action':'FY_BY_CLICKBUTTION',
# 'client':'fanyideskweb',
# 'doctype':'json',
# 'from':'AUTO',
'i':'你好',
# 'keyfrom':'fanyi.web',
    #有问题
'salt':'1509969818095',
'sign':'a25b469fd7c22f83b47f23c2c21995ed',
# 'smartresult':'dict',
'to':'AUTO',
'typoResult':'false',
'version':'2.1',
}

# response = requests.post("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
response = sess.post("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
              headers=headers_base,
              data=tran_data
              )

print(response.text)
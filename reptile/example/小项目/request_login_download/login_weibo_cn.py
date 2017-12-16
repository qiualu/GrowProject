# coding=utf-8

import requests
import time

headers_1 = {
'Host': 'weibo.cn',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

headers_2 = {
'Host': 'passport.weibo.cn',
'Connection': 'keep-alive',
'Content-Length': '184',
'Origin': 'https://passport.weibo.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': '*/*',
'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

# 表单内容
form_data = {
'username':'worio.hainan@163.com',
'password':'Qq94313805',
#'entry':'mweibo',
#'r':'http://weibo.cn/',
#'savestate':'1',
#'mainpageflag':'1',
#'ec':'0',
#'pagerefer':'',
#'loginfrom':'',
#'client_id':'',
#'code':'',
#'qq':'',
#'wentry':'',
#'hff':'',
#'hfp':'',
}

# 生成 session 对象
sess = requests.session()

# 获取 cookie
# sess.get('https://weibo.cn/', headers=headers_1)

# 提交表单登陆
response = sess.post('https://passport.weibo.cn/sso/login',
          headers=headers_2,
          data=form_data)

print(response.text)

#################################################################
'''
# 生成 session 对象
sess = requests.session()
'''

# 获取 cookie
response= sess.get('https://weibo.cn/', headers=headers_1)
time.sleep(2)
with open('weibo.html', 'w') as f:
    f.write(response.text)




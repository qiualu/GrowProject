# coding=utf-8

import requests
import time

headers_1 = {
'Host': 'so.gushiwen.org',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

headers_2 = {
'Host': 'so.gushiwen.org',
'Connection': 'keep-alive',
'Content-Length': '303',
'Cache-Control': 'max-age=0',
'Origin': 'http://so.gushiwen.org',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

# 生成 session 对象
sess = requests.session()


###############################################################
### 通过用户密码登陆，需要手工输入验证码
'''
# 获取 cookie
sess.get('http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx', headers=headers_1)

# 下载验证码
response = sess.get('http://so.gushiwen.org/RandCode.ashx', headers=headers_1)
# 保存验证码
with open('code.png', 'wb') as f:
    f.write(response.content)

# 手工输入验证码，赋值于变量
code = input('请输入验证码>>')

# 表单内容
form_data = {
    'from':'http://so.gushiwen.org/user/collect.aspx',
    'denglu':'登录',
    'from':'http://so.gushiwen.org/user/collect.aspx',
    '__VIEWSTATE':'H2dbNnLxIFAytzlqfQc1JTJLadgzdNdE7uOdVx4nPkPZ28kzi2R4Ewgzo/2enNmQ0uYSlQ6Bvv3bG8Z3gegDwkmqSMe+xzaJY8W27FJMwijwYgk4T0tHJFsR4KE=',
    'code': code,
    '__VIEWSTATEGENERATOR':'C93BE1AE',
    'pwd':'123456',
    'email':'1090509990@qq.com',
}

# 提交表单登陆
response = sess.post('http://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx',
          headers=headers_2,
          data=form_data)
'''

####################################################################
# 直接手工设置 cookie 值，跳过登陆验证码
sess.cookies.set('ASP.NET_SessionId','k1pujgprfq1s02rwujnif2ye')
sess.cookies.set('__qc_wId','100')
sess.cookies.set('codeyzgswso','6e3912dc995c916d')
sess.cookies.set('pgv_pvid','6794896695')
sess.cookies.set('gswEmail','1090509990%40qq.com')
sess.cookies.set('idsShiwen2017','%2c1744%2c72240%2c71634%2c71159%2c49386%2c')
sess.cookies.set('gsw2017user','167606%7c6A5471B38CFFFF27880E4F7E9679CF7A')
sess.cookies.set('Hm_lvt_04660099568f561a75456483228a9516','1509608418')
sess.cookies.set('Hm_lpvt_04660099568f561a75456483228a9516','1509609611')

response = sess.get('http://so.gushiwen.org/user/collect.aspx', headers=headers_1)

#####################################################################

print(response.text)

# with open('gushiwen.html', 'w') as f:
#    f.write(response.text)



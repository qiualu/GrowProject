# coding=utf-8

import requests

# 生成 session 对象
sess = requests.session()

# 使用 session 对象 访问首页
# 目的获取 cookies
# print( { e.name:e.value for e in sess.cookies} )
sess.get('http://www.bing.com/translator/?mkt=zh-CN')
print( { e.name:e.value for e in sess.cookies} )

headers_base = {
#'Host': 'www.bing.com',
#'Connection': 'keep-alive',
# 'Content-Length': '31',
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
#'Origin': 'http://www.bing.com',
#'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Content-Type': 'application/json; charset=UTF-8',
'Referer': 'http://www.bing.com/translator/?mkt=zh-CN',
#'Accept-Encoding': 'gzip, deflate',
#'Accept-Language': 'zh-CN,zh;q=0.8',
}

tran_data = '[{"id":123,"text":"吃饭"}]'.encode('utf-8')

'''
# 手动设置 cookie
sess.cookies.set('mtstkn','WeiZJd4tGMwLFf%2Fhih5ZlcFhKEKqPUAXAMq8LiRzg3wYmR566typO58n0Wl4NgSB')
sess.cookies.set('MicrosoftApplicationsTelemetryDeviceId','a3dafa5e-d481-53a8-96b9-73acbd1c958c')
sess.cookies.set('MicrosoftApplicationsTelemetryFirstLaunchTime','1509536001304')
sess.cookies.set('destLang','en')
sess.cookies.set('dmru_list','da%2Cen')
sess.cookies.set('destDia','en-US')
sess.cookies.set('srcLang','-')
sess.cookies.set('smru_list','')
sess.cookies.set('sourceDia','zh-CN')
sess.cookies.set('_EDGE_V','1')
sess.cookies.set('MUID','1E6E8286E0CC6900340289ABE1106855')
sess.cookies.set('MUIDB','1E6E8286E0CC6900340289ABE1106855')
sess.cookies.set('SRCHD','AF=NOFORM')
sess.cookies.set('SRCHUID','V=2&GUID=E21622FC50A24DBA93299CD99245CA75&dmnchg=1')
sess.cookies.set('SRCHUSR','DOB=20171101')
sess.cookies.set('_SS','SID=3D64FAD3A98360162E13F1FDA85F61A7&HV=1509584433&bIm=757615')
sess.cookies.set('_EDGE_S','mkt=zh-cn&SID=3D64FAD3A98360162E13F1FDA85F61A7')
sess.cookies.set('SRCHHPGUSR','WTS=63645181797&CW=1019&CH=546&DPR=1&UTC=480')
'''

# response = requests.post("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
response = sess.post("http://www.bing.com/translator/api/Translate/TranslateArray?from=-&to=en",
              headers=headers_base,
              data=tran_data
              )

print(response.text)




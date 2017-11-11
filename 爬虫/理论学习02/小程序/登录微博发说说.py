# coding = utf-8

import requests

headers_base = {
'Connection':'keep-alive',
'Cache-Control':'max-age=0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
'DNT':'1',
'Referer':'https://weibo.com/?topnav=1&mod=logo',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':'SINAGLOBAL=1375890276564.22.1498788886006; UM_distinctid=15dc5ac5743e6-0467cc90ac3d86-4d015463-1fa400-15dc5ac574419b; httpsupgrade_ab=SSL; TC-Ugrow-G0=5e22903358df63c5e3fd2c757419b456; login_sid_t=e6723f7cc8c499981257130722671d49; TC-V5-G0=7975b0b5ccf92b43930889e90d938495; WBStorage=82ca67f06fa80da0|undefined; _s_tentry=passport.weibo.com; Apache=9563507431344.926.1510197676832; ULV=1510197676839:28:3:2:9563507431344.926.1510197676832:1510103713627; UOR=v.baidu.com,widget.weibo.com,www.baidu.com; cross_origin_proto=SSL; SSOLoginState=1510197860; SCF=ApqSfDpXv5JlKUf1noLKBQlD-hRAeorCKuMpFnBCYwsizf3CyDP5h1Il5Yely7n5kj9-o7XZYAlIYvG2DWiGEgk.; SUB=_2A253B7o0DeRhGeRM4lER9C7NzD-IHXVUdKz8rDV8PUNbmtAKLRXBkW9-bYivnY0r1N9tIzmfu6tNwvU5GQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbUuEOpGPbax.YHbEYI4W85JpX5K2hUgL.FozE1Ke7Sh5pS0e2dJLoI79pIPHydG-t; SUHB=0FQq7m2wVmquAe; ALF=1541733859; un=1101938064@qq.com; wvr=6; wb_cusLike_2293040173=Y; TC-Page-G0=fd45e036f9ddd1e4f41a892898506007; wb_timefeed_2293040173=1',
}
# 'text':'来自邪恶的小星球',  发说说的内容
data = {
'ajwvr':'6',
'__rnd':'1510214368256',
'location':'v6_content_home',
'text':'来自邪恶的小星球',
'appkey':'',
'style_type':'1',
'pic_id':'',
'tid':'',
'pdetail':'',
'rank':'0',
'rankid':'',
'module':'stissue',
'pub_source':'main_',
'pub_type':'dialog',
'isPri':'0',
'_t':'0',
}
headers2 = {
'Host':'weibo.com',
'Connection':'keep-alive',
'Content-Length':'257',
'Origin':'https://weibo.com',
'X-Requested-With':'XMLHttpRequest',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
'Content-Type':'application/x-www-form-urlencoded',
'Accept':'*/*',
'DNT':'1',
'Referer':'https://weibo.com/qiualu/home?wvr=5',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':'SINAGLOBAL=1375890276564.22.1498788886006; UM_distinctid=15dc5ac5743e6-0467cc90ac3d86-4d015463-1fa400-15dc5ac574419b; httpsupgrade_ab=SSL; TC-Ugrow-G0=5e22903358df63c5e3fd2c757419b456; login_sid_t=e6723f7cc8c499981257130722671d49; TC-V5-G0=7975b0b5ccf92b43930889e90d938495; _s_tentry=passport.weibo.com; Apache=9563507431344.926.1510197676832; ULV=1510197676839:28:3:2:9563507431344.926.1510197676832:1510103713627; cross_origin_proto=SSL; SSOLoginState=1510197860; SCF=ApqSfDpXv5JlKUf1noLKBQlD-hRAeorCKuMpFnBCYwsizf3CyDP5h1Il5Yely7n5kj9-o7XZYAlIYvG2DWiGEgk.; SUB=_2A253B7o0DeRhGeRM4lER9C7NzD-IHXVUdKz8rDV8PUNbmtAKLRXBkW9-bYivnY0r1N9tIzmfu6tNwvU5GQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbUuEOpGPbax.YHbEYI4W85JpX5K2hUgL.FozE1Ke7Sh5pS0e2dJLoI79pIPHydG-t; SUHB=0FQq7m2wVmquAe; ALF=1541733859; un=1101938064@qq.com; wvr=6; TC-Page-G0=fd45e036f9ddd1e4f41a892898506007; wb_timefeed_2293040173=1; wb_cusLike_2293040173=Y; UOR=v.baidu.com,widget.weibo.com,www.baidu.com',
}
url1 = 'https://weibo.com/qiualu/home?wvr=5&lf=reg'
url2 = 'https://weibo.com/aj/mblog/add?ajwvr=6&__rnd=1510214368256 HTTP/1.1'
response = requests.post(url2,headers=headers2,data=data)
print(response.text)
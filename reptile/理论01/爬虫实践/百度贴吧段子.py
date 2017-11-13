import requests
from lxml import etree
import os
#当前目录
# print(os.getcwd())
# print(os.path.abspath(os.curdir))
# print(os.path.abspath('加上的路由目录'))

base_url = os.path.abspath(os.curdir)
headers = {
'Request URL':'https://tieba.baidu.com/p/4772107111',
'Request Method':'GET',
'Status Code':'200 OK (from memory cache)',
'Remote Address':'111.206.76.31:443',
'Referrer Policy':'no-referrer-when-downgrade'
}


# https://tieba.baidu.com/p/4772107111?pn=3
url = 'https://tieba.baidu.com/p/4772107111'

#请求网页
def webpage_requests(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    duanzi = html.xpath('//*[@class="d_post_content j_d_post_content "]/text()')
    write_file(duanzi)

# 写入文件
def write_file(duanzi):
    guolv = []
    with open('段子.txt','a+') as f:
        for d in duanzi:
            if len(d) > 10:
                guolv.append(d)
                d =  d.lstrip()
                f.write(d)
                f.write('\n')

for i in range(1,161):
    url = 'https://tieba.baidu.com/p/4772107111?pn=' + str(i)
    try:
        webpage_requests(url)
    except:
        print('第%s页有点问题,但略过了'%i)
    print('完成第%s页'%i)



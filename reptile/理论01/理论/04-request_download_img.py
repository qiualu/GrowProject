#coding = utf-8
import os
import requests
from lxml import etree


header = {
    'CONNECT clients2.google.com':'443 HTTP/1.1',
    'Host': 'clients2.google.com:443',
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

# response = requests.get('http://www.gandianli.com/file/upload/201611/15/17155929732.png.middle.png',headers=header)
#
# print(response)
# with open('tu.jpg','wb') as f:
#     f.write(response.content)


response = requests.get('http://www.gandianli.com/jiju/',headers = header)
print(response)
html = etree.HTML(response.text)
print(html)
src_list = html.xpath('//img[@class="sell_img"]/@src')
print(src_list)
print(len(src_list))

i = 0
for tu in src_list:
    p = requests.get(tu)
    i += 1
    tupian = 'tupian' + str(i) + '.jpg'
    with open(tupian,'wb') as f:
        f.write(p.content)

# /html/body[@class='fix-header fix-sidebar content-wrapper']/div[@id='wrapper']/div[@id='page-wrapper']/div[@class='container-fluid']/div[@class='row']/div[@class='col-md-12']/div[@class='white-box']/div[@class='row']/div[@class='col-lg-10 col-md-9 col-sm-12 col-xs-12 mail_listing']/div[@class='row']/div[@id='wikiContent']/div[@class='infobox']/table/tbody/tr[2]/td[2]/p

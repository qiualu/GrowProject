import requests
from lxml import etree
import time
import os
base_data = os.path.abspath('02day图片下载')
headers_base = {
'Host': 'www.gandianli.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

'''
# 提交图片url请求
response = requests.get("http://www.gandianli.com/file/upload/201611/15/09181934732.png.thumb.png",headers=headers_base)

# print(response.text)

# 新建打开一个文件
# 将响应数据以二进制的方式写入文件
with open("tu.jpg", 'wb') as f:
    f.write(response.content)
'''

def download_onepage_img(page_url):
    # 获取 html 页面
    response = requests.get(page_url, headers=headers_base)

    # 从获取到的 html 页面中 使用 xpath 提取图片 url 列表
    html = etree.HTML(response.text)
    src_list = html.xpath("//img[@class='sell_img']/@src")

    # 循环遍历每个图片url
    for src in src_list:
        # 提取图片名称
        img_name = src.split('/')[-1]
        print(img_name)
        # 发送请求，获得响应
        img_response = requests.get(src, headers=headers_base)
        # 新建打开一个文件
        # 将响应数据以二进制的方式写入文件
        path = os.path.join(base_data,img_name)
        with open(path, 'wb') as f:
            f.write(img_response.content)

for index in range(1,142):
    page_url = "http://www.gandianli.com/sell/list.php?catid=&page=" + str(index) + \
           "&price=0&thumb=0&vip=0&day=0&order=&list=1"

    time.sleep(2)
    download_onepage_img(page_url)





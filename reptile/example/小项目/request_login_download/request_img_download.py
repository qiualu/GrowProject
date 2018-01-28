# coding = utf-8

import requests
from lxml import etree
import time
import os
headers_base = {
'Host': 'www.gandianli.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

path = os.path.join(os.getcwd(),'img')
'''
# 提交图片url请求
response = requests.get("http://www.gandianli.com/file/upload/201611/15/09181934732.png.thumb.png",
             # headers=headers_base)

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
        print('没东西???')
        # 提取图片名称
        img_name = src.split('/')[-1]
        print(img_name)
        # 发送请求，获得响应
        img_response = requests.get(src, headers=headers_base)
        # 新建打开一个文件
        # 将响应数据以二进制的方式写入文件
        with open(os.path.join(path , img_name), 'wb') as f:
            print("没保存??")
            f.write(img_response.content)

print('开始')
for index in range(1,142):
    print('开始',index)
    page_url = "http://www.gandianli.com/sell/list.php?catid=&page=" + str(index) + \
           "&price=0&thumb=0&vip=0&day=0&order=&list=1"
    print('结束', index)
    time.sleep(2)
    print('开始,下载')
    download_onepage_img(page_url)
    print('开始,下载')






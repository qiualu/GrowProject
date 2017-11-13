# coding=utf-8

import requests
from lxml import etree
import time

headers_base ={
'Host': 'www.douyu.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
}

# 发送请求，接受响应
response = requests.get("https://www.douyu.com/directory/all", headers=headers_base)
# 将html文本格式化成 xpath 可以解析的对象
html = etree.HTML(response.text)
table = []
row = []
# 限制查找内容的标签范围
li_list = html.xpath("//ul[@id='live-list-contentbox']/li")

# 获取首页的第一个主播名
# 为了结束判断提供条件
first_name = html.xpath("//ul[@id='live-list-contentbox']/li[1]//span[@class='dy-name ellipsis fl']/text()")
print("first_name = ", first_name)

# 循环获取 li 标签
# 设置标志, 0 时表示主播名, 1 时表示在看人数
flag = 0
for li in li_list:
    # 获得 主播名 和 观看人数
    info_list = li.xpath(".//span[@class='dy-name ellipsis fl']/text() \
                          | .//span[@class='dy-num fr']/text()")
    # 循环获取每个信息
    for info in info_list:
        # 第一个信息为主播名称
        if not flag :
            # 添加 主播 信息
            row.append(info)
            # 将标志改成 1，下次循环的时候，按 人数 处理
            flag += 1
        else :
            # 添加 人数 信息
            row.append(info)
            # 将一行信息添加到表中
            table.append(row)
            # 清空行
            row = []
            # 将标志改成 0，下次循环的时候，按 主播 处理
            flag = 0

# 注意：
# 网页代码有时并非所见即所得
# 有些代码是通过浏览器运行 js 产生的
# 而 requests 模块并不是 浏览器
# 它只能获取最初的 html 代码
# max_page_num = html.xpath("//div[@id='J-pager']/a[@class='shark-pager-item'][last()]/text()")

index = 1
while True :
    # 每次跳越 n 页
    index += 8

    # 通过 fiddler 获取 ajax 动态发送的请求 url
    # 并发现每页 url 变化规则，循环形成新的 url
    ajax_url = 'https://www.douyu.com/directory/all?page=' + str(index) + '&isAjax=1'

    # 向 ajax url 提交请求，获得响应
    response = requests.get(ajax_url, headers=headers_base)

    # 将html文本格式化成 xpath 可以解析的对象
    html = etree.HTML(response.text)

    # 获取每一页 ajax 加载 的 第一个主播名
    ajax_first_name = html.xpath("//li[1]//span[@class='dy-name ellipsis fl']/text()")
    print(ajax_first_name)
    time.sleep(2)

    # 如果 和 首页的第一个主播名相同，则退出
    if ajax_first_name == first_name:
        break

    # 获得页面所有的 li 元素
    li_list = html.xpath("//li")

    # 遍历每个 li 元素
    for li in li_list:
        # 从一个 li 元素中提取 主播名 和 人数
        info_list = li.xpath(".//span[@class='dy-name ellipsis fl']/text() \
                              | .//span[@class='dy-num fr']/text()")
        # 循环获取每个信息
        for info in info_list:
            # 第一个信息为主播名称
            if not flag :
                # 添加 主播 信息
                row.append(info)
                # 将标志改成 1，下次循环的时候，按 人数 处理
                flag += 1
            else :
                # 添加 人数 信息
                row.append(info)
                # 将一行信息添加到表中
                table.append(row)
                # 清空行
                row = []
                # 将标志改成 0，下次循环的时候，按 主播 处理
                flag = 0

# 打印数据
print(table)






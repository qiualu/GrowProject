# # -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

# driver = webdriver.PhantomJS(executable_path=r"D:\program\Python\phantomjs\bin\phantomjs.exe")
# driver.get('http://www.baidu.com')
# data = driver.title
# print(data)

class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    #可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进
    # allowed_domains = ['xiaochengxu']
    #待爬取的网站列表
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # title = response.xpath('/html/head/title/text()')
        # print(title)
        print('123+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')





# coding=utf-8

import scrapy
import time
class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'

    custom_settings = {
        'ITEM_PIPELINES': {}
    }

    start_urls = ['http://stock.10jqka.com.cn/']
    #进入首页 处理响应
    def parse(self,response):
        # print(response.text)
        #提取子页面的a 元素 列表
        a_list = response.xpath('//div[@id="rzrq"]/table/tbody/tr/td[2]/a')
        #遍历每一个a元素
        for a in a_list:
            # print(a.xpath('./@href').extract()[0])
            # print(a.xpath('./text()').extract()[0])
            #提取子页面的url
            url_str = a.xpath('./@href').extract()[0]
            #向子页面发送 请求
            yield scrapy.Request(url_str,callback=self.download_data)
            break
    #下载子页面数据的函数
    def download_data(self,response):
        print(response.url)
        # print(self.gp_name)
        print(response.meta['gp_name'])
        gp_name = response.meta['gp_name']
        time.sleep(2)
        tr_list = response.xpath("//table[@class='m-table']/tbody/tr")

        for tr in tr_list:
            # print(tr)
            td_list = tr.xpath(".//td/text()").extract()
            td_list[1] = td_list[1].strip()
            # print( '|+|'.join(td_list) )
            with open(gp_name, 'a') as f:
                f.write('|+|'.join(td_list) + '\n')



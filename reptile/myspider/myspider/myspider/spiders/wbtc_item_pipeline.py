# coding=utf-8

# 引入 scrapy 模块
import scrapy
import json
import time
from myspider.items import WbtcItem

# 定义爬虫类
class WbtcItemSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'wbtc_item'

    # allowed_domain = ()

    # 局部 设置项
    custom_settings = {
        #'ITEM_PIPELINES' : {'myspider.pipelines.WbtcPipeline_2': 400}
        'ITEM_PIPELINES' : {}
    }

    # 设置 url
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d200001-0000-1667-c912-e8843d0c8065&ClickID=1']

    index = 2

    #
    wbtc_item = WbtcItem()

    # 处理响应函数
    def parse(self, response):

        # 获取 li 标签列表
        li_list = response.xpath("//ul[@class='listUl']/li[@logr]")

        if not li_list :
            return

        # 遍历 每个 li 变迁
        for li in li_list:
            # 提取 描述 信息
            des = li.xpath(".//div[@class='des']/h2/a/text()") \
                      .extract()[0].strip().split(' ')[0]
            # self.row['des'] = des
            self.wbtc_item['des'] = des

            # 提取 户型 信息
            room_info = li.xpath(".//div[@class='des']/p[@class='room']/text()") \
                           .extract()[0].strip().split(' ')
            # 户型
            room_type = room_info[0]
            # 大小
            room_size = room_info[-1].strip()
            # self.row['room_type'] = room_type
            self.wbtc_item['room_type'] = des
            # self.row['room_size'] = room_size
            self.wbtc_item['room_size'] = room_size

            # 提取 第 1 个 地址信息
            # self.row['addr_1'] = li.xpath(".//div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip()
            self.wbtc_item['addr_1'] = li.xpath(".//div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip()

            # 提取 第 2 个 地址信息
            addr_2 = li.xpath(".//div[@class='des']/p[@class='add']/a[2]/text()").extract()
            if addr_2 :
                # self.row['addr_2'] = addr_2[0].strip()
                self.wbtc_item['addr_2'] = addr_2[0].strip()
            else :
                # self.row['addr_2'] = ''
                self.wbtc_item[' '] = ''

            addr_3 = ''.join(li.xpath(".//p[@class='add']/text()").extract()).strip()
            if addr_3 :
                # self.row['addr_3'] = addr_3
                self.wbtc_item['addr_3'] = addr_3
            else:
                # self.row['addr_3'] = ''
                self.wbtc_item['addr_3'] = ''

            # 提取 价格 信息
            # self.row['money'] = li.xpath(".//div[@class='money']/b/text()").extract()[0].strip()
            self.wbtc_item['money'] = li.xpath(".//div[@class='money']/b/text()").extract()[0].strip()

            # print(self.wbtc_item)
            yield self.wbtc_item

        print("index =========== "+ str(self.index))
        time.sleep(3)

        url_str = 'http://bj.58.com/chuzu/pn' + str(self.index)
        self.index += 30

        # 发送请求
        # 注意：1、在 请求函数前使用 yield；
        #      2、在请求函数中定义一个 callback 函数，这个函数用于除了请求后的响应信息
        yield scrapy.Request(url_str, callback=self.parse)
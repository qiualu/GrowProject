# coding=utf-8

# 引入 scrapy 模块
import scrapy
import json
import time


# 定义爬虫类
class WbtcPagesSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'wbtc_pages'

    # allowed_domain = ()

    # 设置 url
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d200001-0000-1667-c912-e8843d0c8065&ClickID=1']

    table = []
    row = {}
    index = 2

    # 处理响应函数
    def parse(self, response):
        # 获取 li 标签列表
        li_list = response.xpath("//ul[@class='listUl']/li[@logr]")

        # 通过判断页面相关元素是否有值，来确定爬虫是否退出(为空则退出)
        if not li_list :
            with open('table.json', 'w') as f:
                f.write(json.dumps(self.table, ensure_ascii=False))
            # exit(code=0)
            return

        # 遍历 每个 li 变迁
        for li in li_list:
            # 提取 描述 信息
            des = li.xpath(".//div[@class='des']/h2/a/text()") \
                      .extract()[0].strip().split(' ')[0]
            # print(des)
            self.row['des'] = des

            # 提取 户型 信息
            room_info = li.xpath(".//div[@class='des']/p[@class='room']/text()") \
                           .extract()[0].strip().split(' ')
            # 户型
            room_type = room_info[0]
            # 大小
            room_size = room_info[-1].strip()
            # print(room_type)
            self.row['room_type'] = room_type
            # print(room_size)
            self.row['room_size'] = room_size

            # 提取 第 1 个 地址信息
            # print(li.xpath(".//div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip() )
            self.row['addr_1'] = li.xpath(".//div[@class='des']/p[@class='add']/a[1]/text()").extract()[0].strip()

            # 提取 第 2 个 地址信息
            addr_2 = li.xpath(".//div[@class='des']/p[@class='add']/a[2]/text()").extract()
            if addr_2 :
                # print(addr_2[0].strip())
                self.row['addr_2'] = addr_2[0].strip()
            else :
                # print('')
                self.row['addr_2'] = ''

            addr_3 = ''.join(li.xpath(".//p[@class='add']/text()").extract()).strip()
            if addr_3 :
                self.row['addr_3'] = addr_3
            else:
                self.row['addr_3'] = ''

            # 提取 价格 信息
            # print(li.xpath(".//div[@class='money']/b/text()").extract()[0].strip() )
            self.row['money'] = li.xpath(".//div[@class='money']/b/text()").extract()[0].strip()

            # 将每一行加入表中
            self.table.append(self.row)
            # 清空行
            self.row = {}

        print("index =========== "+ str(self.index))
        time.sleep(2)

        url_str = 'http://bj.58.com/chuzu/pn' + str(self.index)
        self.index += 30

        # 发送请求
        # 注意：1、在 请求函数前使用 yield；
        #      2、在请求函数中定义一个 callback 函数，这个函数用于除了请求后的响应信息
        yield scrapy.Request(url_str, callback=self.parse)
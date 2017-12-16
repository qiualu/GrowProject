# coding=utf-8

# 引入 scrapy 模块
import scrapy
import json

# 新建爬虫类
# 继承 scrapy.Spider
class FirstSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'firstspider'

    # 添加请求 url
    start_urls = ['http://www.kexuejisuan.com']

    # 默认情况下，scrapy 会以get的方式发送 start_urls 中的 url
    # 定义处理响应函数，函数名必须为 parse
    def parse(self, response):
        print(response.text)


# 定义爬虫类
class WbtcSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'wbtc'

    # allowed_domain = ()

    # 设置 url
    start_urls = ['http://bj.58.com/chuzu/?PGTID=0d200001-0000-1667-c912-e8843d0c8065&ClickID=1']

    table = []
    row = {}

    # 处理响应函数
    def parse(self, response):
        # 获取 li 标签列表
        li_list = response.xpath("//ul[@class='listUl']/li[@logr]")
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

            # 提取 价格 信息
            # print(li.xpath(".//div[@class='money']/b/text()").extract()[0].strip() )
            self.row['money'] = li.xpath(".//div[@class='money']/b/text()").extract()[0].strip()

            # 将每一行加入表中
            self.table.append(self.row)
            # 清空行
            self.row = {}

        # print(self.table)
        # 将数据保存成 json 文件
        with open('wbtc.json','w') as f:
            # 注意，要加上参数 ensure_ascii=False，避免中文变成 Unicode 格式
            f.write(json.dumps(self.table, ensure_ascii=False))



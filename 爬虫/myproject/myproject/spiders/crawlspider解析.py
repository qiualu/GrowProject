import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

# 爬取一般网站常用的spider。其定义了一些规则(rule)来提供跟进link的方便的机制。
# 也许该spider并不是完全适合您的特定网站或项目，但其对很多情况都使用。
# 因此您可以以其为起点，根据需求修改部分方法。当然您也可以实现自己的spider。

class MyCrawlSpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    # 除了从Spider继承过来的(您必须提供的)属性外，其提供了一个新的属性:
    #一个包含一个(或多个) Rule 对象的集合(list)。 每个 Rule 对爬取网站的动作定义了特定表现。
    # Rule对象在下边会介绍。
    # 如果多个rule匹配了相同的链接，则根据他们在本属性中被定义的顺序，第一个会被使用
    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)

        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
    
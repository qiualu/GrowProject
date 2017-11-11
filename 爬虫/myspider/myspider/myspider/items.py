# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class MyspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class WbtcItem(scrapy.Item):
    des = scrapy.Field()
    room_type = scrapy.Field()
    room_size = scrapy.Field()
    addr_1 = scrapy.Field()
    addr_2 = scrapy.Field()
    addr_3 = scrapy.Field()
    money = scrapy.Field()



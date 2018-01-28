# -*- coding： utf-8 -*-
import scrapy
from ..items import X01Item

class X01Spider(scrapy.Spider):
    name = 'X01'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.']




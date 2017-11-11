#!/usr/bin/env python
# coding : utf-8

from lxml import etree

def parse(html):
    '''python 3 默认utf-8'''
    doc = etree.HTML(html)
    title = doc.xpath('//h2[@id="activity-name]/text()"')
    date = doc.xpath('//em[@id="past-date"]/text()')
    auth = doc.xpath('//em[@id="past-date"]/@href')






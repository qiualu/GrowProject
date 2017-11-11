from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractor import LinkExtractor
import subprocess
import os
import time


path = os.path.abspath('下载')

class BizhiSpider(CrawlSpider):
    name = 'bizhi'
    start_urls = ['https://www.xnmei.com/']

    bizhi_link = LinkExtractor(allow=r'/tuku/.*html$')
    # /html/body/div[2]/div[1]/div[8]/ul/li/a/@href
    #https://tuku.xnmei.com/d/file/bigpic/2017/03/19/4ostmeh3u0h.jpg

    rules = (
        Rule(bizhi_link,callback='download_img',follow=True)
    )

    def download_img(self, response):
        img_url = response.xpth('//a[@id="RightUrl"]/img/@src').extract()
        print(img_url)
        time.sleep(3)
        subprocess.Popen(['wget',img_url,'-P',path])


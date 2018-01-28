
# 本篇教程中将带您完成下列任务:

#  1 创建一个Scrapy项目
#  2 定义提取的Item
#  3 编写爬取网站的 spider 并提取 Item
#  4 编写 Item Pipeline 来存储提取到的Item(即数据)

# ***********   创建项目  **************
'''
# 在开始爬取之前，您必须创建一个新的Scrapy项目。 进入您打算存储代码的目录中，运行下列命令:
# >>>>>   scrapy startproject myproject
# 该命令将会创建包含下列内容的 myproject 目录:

# scrapy.cfg: 项目的配置文件
# myproject/: 该项目的python模块。之后您将在此加入代码。
# myproject/items.py: 项目中的item文件.
# myproject/pipelines.py: 项目中的pipelines文件.
# myproject/settings.py: 项目的设置文件.
# myproject/spiders/: 放置spider代码的目录.
'''
# ***********   定义Item  **************
'''
# Item 是保存爬取到的数据的容器；其使用方法和python字典类似， 
# 并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。

类似在ORM中做的一样，您可以通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field 
的类属性来定义一个Item。 (如果不了解ORM, 不用担心，您会发现这个步骤非常简单)

首先根据需要从dmoz.org获取到的数据对item进行建模。 我们需要从dmoz中获取名字，url，
以及网站的描述。 对此，在item中定义相应的字段。编辑 myproject 目录中的 items.py 文件:

import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

一开始这看起来可能有点复杂，但是通过定义item， 您可以很方便的使用Scrapy的其他方法。而这些方法需要知道您的item的定义。

'''
# ***********   编写第一个爬虫(Spider)  **************

import scrapy














































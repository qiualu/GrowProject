import  scrapy

# Spider类定义了如何爬取某个(或某些)网站。
# 包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。
# 换句话说，Spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方。
#spider来说，爬取的循环类似下文:
#1  以初始的URL初始化Request，并设置回调函数。
#   当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数。
#       spider中初始的request是通过调用 start_requests() 来获取的。
#       start_requests() 读取 start_urls 中的URL， 并以 parse 为回调函数生成 Request 。
#2  在回调函数内分析返回的(网页)内容，返回 Item 对象或者 Request 或者一个包括二者的可迭代容器。
#   返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)。
#3  在回调函数内，您可以使用 选择器(Selectors)
# (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item。
#4 最后，由spider返回的item将被存到数据库(由某些 Item Pipeline 处理)或使用 Feed exports 存入到文件中。
class Myspider(scrapy.Spider):
    #定义爬取名字; 爬取 scrapy crawl myspider
    name = 'myspider'
    # name
    #定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。 不过您可以生成多个相同的spider实例(instance)，这没有任何限制。 name是spider最重要的属性，而且是必须的。
    # 如果该spider爬取单个网站(single domain)，一个常见的做法是以该网站(domain)(加或不加 后缀 )来命名spider。 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为 mywebsite 。

    # Spider参数
    # 在运行crawl时添加 - a可以传递Spider参数: scrapy crawl myspider -a category=electronics
    #Spider在构造器(constructor)中获取参数:
    # def __init__(self, category=None, *args, **kwargs):
    #     super(Myspider, self).__init__(*args, **kwargs)
    #     self.start_urls = ['http://www.example.com/categories/%s' % category]

    #**** 可选。包含了spider允许爬取的域名(domain)列表(list)。 当OffsiteMiddleware启用时， 域名不在列表中的URL不会被跟进。
    allowed_domains = []

    #**** URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。
    start_urls = ['http://www.baidu.com']

    # 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。
    def start_requests(self):
        #当spider启动爬取并且未制定URL时，该方法被调用。 当指定了URL时，make_requests_from_url() 将被调用来创建Request对象。 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。
        # 该方法的默认实现是使用start_urls的url生成Request。
        return [scrapy.FormRequest("http://www.example.com/login",
                               formdata={'user': 'john', 'pass': 'secret'},
                               callback=self.logged_in)]

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass
    #该方法接受一个URL并返回用于爬取的 Request 对象。 该方法在初始化request时被 start_requests() 调用，也被用于转化url为request。
    #默认未被复写(overridden)的情况下，该方法返回的Request对象中， parse() 作为回调函数，dont_filter参数也被设置为开启。 (详情参见 Request).
    def make_requests_from_url(self,url):
        return 'ok'

    # 当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法。
    def parse(self,response):
        #parse 负责处理response并返回处理的数据以及(/或)跟进的URL。 Spider 对其他的Request的回调函数也有相同的要求。
        #该方法及其他的Request回调函数必须返回一个包含 Request 及(或) Item 的可迭代的对象。
        #参数:	response (Response) – 用于分析的response
        pass
    #
    #log(message[, level, component])
    #使用 scrapy.log.msg() 方法记录(log)message。
    # log中自动带上该spider的 name 属性。 更多数据请参见 Logging 。


    def closed(self,reason):
        # 当spider关闭时，该函数被调用。 该方法提供了一个替代调用signals.connect()来监听spider_closed信号的快捷方式。
        pass





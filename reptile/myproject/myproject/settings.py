# -*- coding: utf-8 -*-

# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myproject'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 通过在用户代理上识别自己(和你的网站)来负责地爬行
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'

# Obey robots.txt rules
# 遵守机器人。三种规则
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置由Scrapy执行的最大并发请求(默认为16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
#为同一网站的请求配置一个延迟(默认为0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#请参阅自动油门设置和文档
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#下载延迟设置仅为其中之一:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#禁用cookie(默认启用)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#禁用Telnet控制台(默认启用)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认的请求标头
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# 启用或禁用蜘蛛中间件
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myproject.middlewares.MyprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# 启用或禁用下装程序中间件
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.MyCustomDownloaderMiddleware': 543,  #键为中间件类的路径，值为中间件的顺序
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None, #禁止内置的中间件
# }

# Enable or disable extensions
# 启用或禁用扩展
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# 配置项管道
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'myproject.pipelines.MyprojectPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# 启用和配置自动油门扩展(默认情况下禁用)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to each remote server
# 与每个远程服务器并行发送的请求的平均数量应该是并行的。
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 允许对收到的每个响应显示节流统计数据
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# 启用和配置HTTP缓存(默认情况下禁用)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

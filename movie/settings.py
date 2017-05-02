# -*- coding: utf-8 -*-

# Scrapy settings for movie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
   'Cookie':'gr_user_id=ab75ebba-b3d7-4bda-be80-b9c3f4c1bf60; bid=i6R3AfCfEu0; __ads_session=cblr7dR73wh1fnoQDwA=; ll="108296"; _ga=GA1.2.2143097302.1449387025; _gid=GA1.2.2020786551.1493736649; ps=y; ue="dakgzhu@foxmail.com"; dbcl2="50573392:MZjfcrlqIKQ"; ck=uWRn; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1493736693%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E8%2580%2581%25E7%25AC%25A0%22%5D; ap=1; __yadk_uid=vS6dkog0Xka66JeHhCcXh69GAQiaVOAy; _pk_id.100001.4cf6=74c9cd8ef14a63fd.1477054680.33.1493738213.1492950179.; _pk_ses.100001.4cf6=*; __utma=30149280.2143097302.1449387025.1493123848.1493736640.123; __utmb=30149280.8.9.1493737435501; __utmc=30149280; __utmz=30149280.1492317958.115.37.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.5057; __utma=223695111.556368422.1455425326.1492949953.1493736693.66; __utmb=223695111.0.10.1493736693; __utmc=223695111; __utmz=223695111.1492949953.65.49.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=C59DFB3B9F638A485A1A6F0C15A804DB|78546bf67c2719699b42a88b2588ffa5',
   'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movie.middlewares.MovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'movie.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'movie.pipelines.MoviePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

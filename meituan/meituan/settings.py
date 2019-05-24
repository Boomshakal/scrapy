# -*- coding: utf-8 -*-

# Scrapy settings for meituan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meituan'

SPIDER_MODULES = ['meituan.spiders']
NEWSPIDER_MODULE = 'meituan.spiders'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'meituan'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meituan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

HTTPERROR_ALLOWED_CODES = [403]  #防止403崩溃
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
  'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'meituan.middlewares.MeituanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'meituan.middlewares.MeituanDownloaderMiddleware': 543,
    'meituan.middlewares.CookiesMiddleware': 542,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'meituan.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#COOKIES = '_lxsdk_cuid=16a07408884c8-0a9c440cb13bab-1a201708-240000-16a07408884c8; client-id=c9bcc3ab-fbb8-44d6-81af-fc74deb71c8a; ci=191; rvct=191%2C469%2C1198%2C693%2C457; mtcdn=K; lsu=; _lxsdk=16a07408884c8-0a9c440cb13bab-1a201708-240000-16a07408884c8; u=349671443; n=ilx187682559; lt=p6XGMhC1YW-FTF00B7jzZwZWDoMAAAAAPQgAAJO71L6Jt4imZjAgRV2adL4cDTEtyip4d14TIyoFRaN8dIJmf2BGputGAWZ4zOWL5A; token2=p6XGMhC1YW-FTF00B7jzZwZWDoMAAAAAPQgAAJO71L6Jt4imZjAgRV2adL4cDTEtyip4d14TIyoFRaN8dIJmf2BGputGAWZ4zOWL5A; uuid=4444f74dc8c441fd8f94.1554950855.3.0.0; unc=ilx187682559; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=45579675.1554899851564.1554951826198.1554962371447.8; _lxsdk_s=16a0afad0c4-d97-991-f15%7C%7C4'#cookie值
PROXY_URL = ''#ip代理池地址
COOKIES = '__mta=251567673.1554967589221.1554967589221.1555221540825.2; _lxsdk_cuid=16a07408884c8-0a9c440cb13bab-1a201708-240000-16a07408884c8; mtcdn=K; lsu=; rvct=30%2C191%2C469%2C1198%2C693%2C457; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; iuuid=B279A7F8F0F1E559ADFD8ADBB40D9C0E1C67DE8E60C3E8A15B2DBDE22BBF0198; isid=997EFE58B53FD57DF04AC04DB2C68410; oops=p6XGMhC1YW-FTF00B7jzZwZWDoMAAAAAPQgAAJO71L6Jt4imZjAgRV2adL4cDTEtyip4d14TIyoFRaN8dIJmf2BGputGAWZ4zOWL5A; logintype=normal; _lxsdk=B279A7F8F0F1E559ADFD8ADBB40D9C0E1C67DE8E60C3E8A15B2DBDE22BBF0198; webp=1; __utmz=74597006.1554967476.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/xing851483876/article/details/81842329; ci=191; cityname=%E5%8F%B0%E5%B7%9E; _hc.v=470dc91c-7b7f-7c69-033c-46568c7ed426.1554967589; IJSESSIONID=wyjaa95oi3at1hpae9hy1wn97; u=349671443; __utma=74597006.869701978.1554967476.1554967476.1555221475.2; __utmc=74597006; ci3=1; idau=1; latlng=28.649353,121.421615,1555221536382; __utmb=74597006.5.9.1555221539901; i_extend=C_b1Gimthomepagecategory11H__a; client-id=4098cbf4-7787-4792-9c32-1650df27365d; uuid=a6bda921-a8f3-41a1-b2b6-338f7330c021; p_token=p6XGMhC1YW-FTF00B7jzZwZWDoMAAAAAPQgAAJO71L6Jt4imZjAgRV2adL4cDTEtyip4d14TIyoFRaN8dIJmf2BGputGAWZ4zOWL5A; logan_custom_report=; _lxsdk_s=16a1a6c6e80-448-0a0-b9b%7C%7C11; logan_session_token=meiq73xi3rfcjhdsmp6e'
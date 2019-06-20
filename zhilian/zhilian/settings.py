# -*- coding: utf-8 -*-

# Scrapy settings for zhilian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhilian'

SPIDER_MODULES = ['zhilian.spiders']
NEWSPIDER_MODULE = 'zhilian.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhilian (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Referer': 'https://rd5.zhaopin.com/custom/search/result',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

COOKIES = [
    {'x-zp-device-id': 'baf4cd2f5f4f91805eefd5af9933d9cf',
     'acw_tc': '2760821415603902374261539e7a2baafb02477164dec681226df1d41e59ca', 'rd_resume_srccode': '402101',
     'x-zp-client-id': 'be2de5ef-563b-4006-acb4-f73ecd427a87', 'sajssdk_2015_cross_new_user': '1',
     'sts_deviceid': '16b4eca972d5d6-057f59ed9271b1-e353165-1638720-16b4eca972f516', 'dywec': '95841923',
     'dywez': '95841923.1560395028.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined',
     '__utmc': '269921210', '__utmz': '269921210.1560395028.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
     'urlfrom': '121113803', 'urlfrom2': '121113803', 'adfbid': '0', 'adfbid2': '0', 'sts_sg': '1',
     'sts_chnlsid': '121113803',
     'zp_src_url': 'https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAs0pEf7I00000r2_AdC00000X8254C.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15H61mWbsPyfvnj0suhnvPjm0IHYLnYw7PDNAn1T1nHf3nDRdfYmdrjb1PbmswDfsPYRknsK95gTqFhdWpyfqn1cznWmzPH63PBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Y1nWT1ns%26tpl%3Dtpl_11535_18778_14772%26l%3D1511763170%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3222625886_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D241%26ie%3Dutf-8%26f%3D8%26tn%3Dbaiduhome_pg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26inputT%3D1365',
     'login-type': 'b', 'zp-route-meta': 'uid=132787351,orgid=25272202', 'login_point': '25272202', 'promoteGray': '',
     'NTKF_T2D_CLIENTID': 'guest8DCEC7C1-BD7E-64E2-4969-4ECB5268176C',
     'nTalk_CACHE_DATA': '{uid:kf_9051_ISME9754_25272202,tid:1560395076200815}',
     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22132787351%22%2C%22%24device_id%22%3A%2216b4eca95c314c-0f6919a300b3ad-e353165-1638720-16b4eca95c474%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAs0pEf7I00000r2_AdC00000X8254C.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15H61mWbsPyfvnj0suhnvPjm0IHYLnYw7PDNAn1T1nHf3nDRdfYmdrjb%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216b4eca95c314c-0f6919a300b3ad-e353165-1638720-16b4eca95c474%22%7D',
     'at': '57b2c4b30eff4a50ba689ca0ad113bac', 'rt': '9d41bb1d0a734f40b3a0c836e4285c0b', 'diagnosis': '0',
     'sts_evtseq': '1', 'sts_sid': '16b4fd87d9316e-036d55bd8ca9e4-e353165-1638720-16b4fd87d942a',
     'rd_resume_actionId': '1560412716544132787351',
     'dywea': '95841923.3887055483229229000.1560395028.1560395028.1560412717.2', 'dyweb': '95841923.1.10.1560412717',
     '__utma': '269921210.1727489822.1560395028.1560395028.1560412717.2', '__utmt': '1',
     '__utmb': '269921210.1.10.1560412717'}
]

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'zhilian.middlewares.RandomCookieMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhilian.middlewares.ZhilianDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'zhilian.pipelines.ZhilianPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

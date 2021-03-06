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
    {'acw_tc': '2760828a15608582884383085e2ae8048d2aac2f8a25aa341ff2feb2d93e3a', 'urlfrom2': '121113803',
     'adfbid2': '0', 'x-zp-client-id': '62adf250-80ba-46d6-9ad1-e1de31d7874a',
     'sts_deviceid': '16b7e05fef6113-05a10ad6eee9cb-1a29140e-1637760-16b7e05fef71b9',
     'x-zp-device-id': 'b2529b46480a6f889d6a515ad9096a64', 'JSloginnamecookie': '15168633879', 'JSShowname': '""',
     'JSpUserInfo': '3d692e695671467155775b755a6a507541775a695a6958714e715e772575276a597541775d695b695d714f7153775a755a6a5c754777516951692e713a7158770575006a0c750577016907690271197114771875296a03751d77096903690771597106770675046a5f7523773c6957695a714c7124773d75546a51755d775a694a695a7147715f775975526a25753c7755695b695071227124775475236a2d7542775b695e695a71457155775a75506a50754b773d693e69567146715e773a75206a5975407753693f693b71397158770675076a5375027719695e69057107711f7719751d6a0e7517770e690e691a7144711d770c75516a117508770b690e6958710e710c770075526a6',
     'uiioit': '21793065596409375477066456744d7454645638076444345d654f7936652064053754770f643',
     'NTKF_T2D_CLIENTID': 'guest26E8C0CA-19EC-FA59-2D08-8C5CDC9D5669', 'promoteGray': '', 'diagnosis': '0',
     'login_point': '25272202', 'urlfrom': '121113803', 'adfbid': '0', 'registerGroup': 'psapi', 'sts_sg': '1',
     'sts_sid': '16b9805ba5b4e4-048bc4f3f200c4-3f71045b-1637760-16b9805ba5c3cb', 'sts_chnlsid': '121113803',
     'zp_src_url': 'https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsKRxKwI00000r2_AdC00000X8254C.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15yfvmvRzrHbvnj0snj03nhD0IHYsf17arRfsfWNjrHc3PW7KP1n1fWw7n1-KfRNKfYP7r0K95gTqFhdWpyfqn1cznWmzPH63PBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1YzPW04rf%26tpl%3Dtpl_11535_18778_14772%26l%3D1511763170%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3222625886_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D241%26ie%3Dutf-8%26f%3D3%26tn%3Dbaiduhome_pg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26inputT%3D3334',
     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22132787351%22%2C%22%24device_id%22%3A%2216b7e06010f8a9-0ed7ff34b7fac6-1a29140e-1637760-16b7e060110971%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsKRxKwI00000r2_AdC00000X8254C.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15yfvmvRzrHbvnj0snj03nhD0IHYsf17arRfsfWNjrHc3PW7KP1n1fWw%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216b7e06010f8a9-0ed7ff34b7fac6-1a29140e-1637760-16b7e060110971%22%7D',
     'dywea': '95841923.1886521082029241900.1561187554.1561427951.1561623644.3', 'dywec': '95841923',
     'dywez': '95841923.1561623644.3.3.dywecsr=landing.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/register',
     '__utma': '269921210.1306712621.1561187555.1561427951.1561623644.3', '__utmc': '269921210',
     '__utmz': '269921210.1561623644.3.3.utmcsr=landing.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/register',
     '__utmt': '1', 'at': '5d889e6f218c492caf561b2b4874d280', 'rt': 'fca207b42fca485a9f221832e3e6b8bd',
     'login-type': 'b', 'zp-route-meta': 'uid=132787351,orgid=25272202',
     'FSSBBIl1UgzbN7N443S': 'Ta8PX.v3p8ti65bOXeTna6met7VA3AwvRpqS1dETKvlLuBtknKNqew0_GiePuVSA',
     'nTalk_CACHE_DATA': '{uid:kf_9051_ISME9754_25272202,tid:1561623684234788}', 'sts_evtseq': '2',
     'dyweb': '95841923.2.10.1561623644', '__utmb': '269921210.2.10.1561623644',
     'FSSBBIl1UgzbN7N443T': '3XvqJnmwCwENVyzUpRHBcZr59lu3u0Yo.dihHQNgBXGkLleRiMUaKmC7pOVoffZ4.HD2_OPQ7r2.8x.f3JnB7YTIluOi1YWNiUNOpZODjU6W_PwWdWyqMTtvQ38xOybiE5zhXcJlHL6T69EechtMCQ2z.v86TFxmXFS.FjE7XclKELZXm3hPCMGmE3IHkJFEG3cLHuTVS5JJGie.IlgtssXm7v9tvkYPzWcMamXKMhDCJ7q81N50IDxv85Z9sJ2BBeOBpVbC3OKWHGo47HUCclhTF2dyOTWmyS.O0HnaQuGZ9syvhppbbawdn0R6Pm0WSJOqsk.7vqxQt0If79oXr_Hh0b5sCfszR7_QK00y5vh83aa'}

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

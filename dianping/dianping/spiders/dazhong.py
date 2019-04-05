# -*- coding: utf-8 -*-
import scrapy


class DazhongSpider(scrapy.Spider):
    name = 'dazhong'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/zhejiangtaizhou/ch10/r3971']

    def parse(self, response):
        print(response.text)

# -*- coding: utf-8 -*-
import scrapy


class GzSpider(scrapy.Spider):
    name = 'gz'
    allowed_domains = ['gz.eywedu.com/zhouzhoulieguozhuan/']
    start_urls = ['http://gz.eywedu.com/zhouzhoulieguozhuan']

    def parse(self, response):
        print(response.text)

# -*- coding: utf-8 -*-
import scrapy


class BoardSpider(scrapy.Spider):
    name = 'board'
    allowed_domains = ['q.10jqka.com.cn']
    start_urls = ['http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/']

    def parse(self, response):
        print(response.text)

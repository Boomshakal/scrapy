# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree

class YingpingSpider(scrapy.Spider):
    name = 'yingping'
    allowed_domains = ['www.movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26394152/comments?start=0&limit=20&sort=new_score&status=P&comments_only=1']

    def parse(self, response):
        rsp=json.loads(response.text)
        html=etree.HTML(rsp['html'])
        yingping=html.xpath('//span[@class="short"]/text()')
        print(yingping)



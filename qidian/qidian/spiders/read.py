# -*- coding: utf-8 -*-
from scrapy import Spider,Request

from qidian.items import QidianItem


class ReadSpider(Spider):
    name = 'read'
    allowed_domains = ['read.qidian.com']
    start_urls = ['https://read.qidian.com/chapter/gunqLjJgXxGt-wSl2uB4dQ2/Z_6wj9yponT4p8iEw--PPw2']

    def parse(self, response):
        item=QidianItem()
        content=[]
        chaptername=response.xpath('//h3[@class="j_chapterName"]/text()').extract_first()
        contents=response.xpath('//div[@class="read-content j_readContent"]')
        text=contents.xpath('./p/text()').extract()
        for t in text:
            content.append(t.strip())

        item['content'] = content
        item['chaptername']=chaptername


        yield item

        next_page = response.xpath('//a[@id="j_chapterNext"]/@href').extract_first()
        if next_page :
            url= 'https:' + next_page
            yield Request(url=url,callback=self.parse)

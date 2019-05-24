# -*- coding: utf-8 -*-
from  scrapy import  Spider,Request

from meizitu.items import MeizituItem


class PhotoSpider(Spider):
    name = 'photo'
    #allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/page/2']

    def parse(self, response):
        #print(response.text)
        results=response.xpath('//div[@class="postlist"]/ul/li')
        for result in results:
            url=result.xpath('./a/@href').extract_first()

            # print(url)
            yield Request(url,callback=self.parse_photo)

        next_page = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        #print(next_page)
        yield Request(next_page,callback=self.parse)

    def parse_photo(self, response):
        image=response.xpath('//div[@class="main-image"]/p/a')
        title = response.xpath('//h2[@class="main-title"]/text()').extract_first()
        #print(title)
        src=image.xpath('./img/@src').extract_first()

        item=MeizituItem()
        item['src']=src
        item['title']=title
        yield item

        next_page = image.xpath('./@href').extract_first()
        #print(next_page)
        yield Request(next_page,callback=self.parse_photo,dont_filter=False)




# -*- coding: utf-8 -*-
from scrapy import Spider,Request

from lianjia.items import LianjiaItem


class HouseSpider(Spider):
    name = 'house'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://cq.lianjia.com/ershoufang']
    base_url = 'https://cq.lianjia.com/ershoufang'
    number = 2
    def parse(self, response):
        # print(response.text)
        results = response.xpath('//li[@class="clear LOGCLICKDATA"]/div')
        #print(len(results))

        for result in results:
            item=LianjiaItem()
            item['title'] = result.xpath('./div[@class="title"]/a/text()').extract()
            item['address'] = result.xpath('./div[@class="address"]/div/a/text()').extract()
            item['price'] = result.xpath('./div[@class="priceInfo"]/div/span/text()').extract()
            item['follow'] = result.xpath('./div[@class="followInfo"]/text()').extract()
            item['tag'] = result.xpath('./div[@class="tag"]/span/text()').extract()

            yield item

        next_page = self.base_url + '/pg' + str(self.number)
        self.number+=1
        yield Request(next_page,callback=self.parse)

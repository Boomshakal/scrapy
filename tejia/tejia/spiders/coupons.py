# -*- coding: utf-8 -*-
import json
from time import sleep

from scrapy import Spider,Request

from tejia.items import TejiaItem


class CouponsSpider(Spider):
    name = 'coupons'
    #allowed_domains = ['http://mai.sogou.com/tejia/coupons/']
    start_url ='http://mai.sogou.com/tejia/m/couponApi.php?type=salelist&page={}&platform=pc&priceType=0&cateid=0'
    page=1
    def start_requests(self):
        yield Request(url=self.start_url.format(self.page),callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text).get('data')

        for i in result:
            print(i)
            item = TejiaItem()
            for field in item.fields:
                if field in i.keys():
                    item[field]=i.get(field)
            yield item

        if self.page<10:
            self.page=self.page+1
            next_page_url=self.start_url.format(self.page)
        else:
            return
        #sleep(2)
        yield Request(next_page_url,self.parse)


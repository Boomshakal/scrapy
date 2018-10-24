# -*- coding: utf-8 -*-
import json
import re

import scrapy

from tejia.items import TejiaItem


class CouponsSpider(scrapy.Spider):
    name = 'coupons'
    #allowed_domains = ['http://mai.sogou.com/tejia/coupons/']
    start_urls = ['http://mai.sogou.com/tejia/coupons/']

    def parse(self, response):
        pattern=re.compile("sogou_coupon_data =(.*?)</script>",re.S)
        result=re.findall(pattern,response.text)
        print(result[0].encode("UTF-8").decode('UTF-8'))


# -*- coding: utf-8 -*-
import random
import re
import time

import scrapy

from zhilian.settings import COOKIES


class DonghuaSpider(scrapy.Spider):
    name = 'donghua'
    # allowed_domains = ['https://rd5.zhaopin.com/api/rd/search/resumeList?_=1560391053140']
    item_url = 'https://rd5.zhaopin.com/api/rd/search/resumeList?_={time}&x-zp-page-request-id={request_id}{time}-{number}&x-zp-client-id={client_id}'

    start_urls = ['https://rd5.zhaopin.com/custom/search/result']

    # def start_requests(self):
    #     url = 'https://passport.zhaopin.com/org/login'
    #
    #     yield scrapy.FormRequest(
    #         url=url,
    #         formdata={
    #             "accountName":"hzwanh","password":"Wheng168168"
    #         },
    #         callback=self.parse
    #     )
    #
    # def parse(self, response):
    #     print(response.body.decode('utf-8'))


    def parse(self, response):
        # print(response.text)
        request_id = re.findall('zpPageRequestId = "(.*?)"', response.text)[0]
        load_time = str(int(time.time() * 1000))
        number = str(int(random.random() * 1000000))
        client_id = COOKIES[0]['x-zp-client-id']

        url = self.item_url.format(request_id=request_id, time=load_time, number=number, client_id=client_id)
        print(url)
        yield scrapy.FormRequest(
            url=url,
            formdata={"start": '1', "rows": '30', "S_DISCLOSURE_LEVEL": '2',
                      "S_EXCLUSIVE_COMPANY": "杭州万恒会计服务有限公司;杭州万恒会计服务有限公司;杭州万恒会计服务有限公司", "S_KEYWORD": "动画",
                      "S_DATE_MODIFIED": "181213,190613", "S_CURRENT_CITY": "653", "S_ENGLISH_RESUME": "1",
                      "isrepeat": '1', "sort": "complex_v15"},
            callback=self.parse_item
        )

    def parse_item(self, response):
        print(response.text)

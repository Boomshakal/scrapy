# -*- coding: utf-8 -*-
import json

from scrapy import Spider,Request

from sleepnubmer.items import SleepnubmerItem
from sleepnubmer.latitude_longitude import location

class StoresSpider(Spider):
    name = 'stores'
    # allowed_domains = ['www.sleepnumber.com']
    loc = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
         'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
         'Maryland', 'Massachusettes', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
         'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'New Mexico', 'North Carolina', 'North Dakota', 'Ohio',
         'Oklahoma', 'Oregon', 'Pennslyvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
         'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

    url_base = 'https://www.sleepnumber.com/api/1/find-mattress-stores?latitude={latitude}&longitude={longitude}'
    # start_urls =['https://stores.sleepnumber.com/ia/west-des-moines/6630-mills-civic-parkway.html']
    def start_requests(self):
        for i in self.loc:
            latitude=location(i).split(',')[0]
            longitude=location(i).split(',')[1]

            yield Request(url=self.url_base.format(latitude=latitude,longitude=longitude),callback=self.parse_stores)

    def parse_stores(self, response):
        results=json.loads(response.text)
        # print(results)
        for result in results:
            url=result['url']
            #print(url)
            yield Request(url=url,callback=self.parse)

    def parse(self,response):
        result=response.xpath('//div[@class="col-md-3 col-sm-6 col-xs-12 col-md-offset-1 Location-info"]')
        title=result.xpath('.//div[@class="col-xs-12"]/h1/div/text()').extract()
        # rating=result.xpath(".//a[@class='bv-rating bv-text-link bv-popup-target bv-focusable']/span/text()").extract()
        location=result.xpath(".//div[@class='col-sm-12']/div/text()").extract()
        address = result.xpath(".//div[@class='c-location-info-address']/address/div/span/text()").extract()[:2]
        abbr=result.xpath(".//div[@class='c-AddressRow']/abbr/text()").extract_first()
        city=result.xpath(".//div[@class='c-AddressRow']/span[@class='c-address-city']/text()").extract_first()
        post=result.xpath(".//div[@class='c-AddressRow']/span[@class='c-address-postal-code']/text()").extract_first()
        phone = result.xpath(".//div[@class='c-location-info-phone-wrapper']/div/div/div/span/text()").extract_first()
        item=SleepnubmerItem()
        item['title']=title
        item['address_info']=location+address
        item['abbr']=abbr
        item['city']=city
        item['post']=post
        item['phone']=phone

        yield item


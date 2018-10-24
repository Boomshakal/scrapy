# -*- coding: utf-8 -*-

from scrapy import Request,Spider

from jindong.items import JindongItem


class PhoneSpider(Spider):
    name = 'phone'
    #allowed_domains = ['https://search.jd.com/Search']
    start_urls = []
    for page in range(1,10):
        start_urls.append('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page={}&click=0'.format(page))



    def parse(self, response):
            phones=response.xpath("//div[@class='gl-i-wrap']")

            #print(len(phones),phones)

            for phone in phones:
                #print(date.extract())
                item=JindongItem()
                item['name']=phone.xpath('./div/a/em/text()').extract()
                item['price']=phone.xpath('./div[@class="p-price"]/strong/i/text()').extract()
                url=phone.xpath('./div/a/@href').extract_first()
                if url[0:5]=='https' :
                    item['url']=url
                else:
                    item['url']='https:'+phone.xpath('./div/a/@href').extract_first()

                yield item
                #yield Request(url=url,callback=self.parse_detail)








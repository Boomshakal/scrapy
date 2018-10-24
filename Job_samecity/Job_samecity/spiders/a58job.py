# -*- coding: utf-8 -*-
from scrapy import Spider,Request

from Job_samecity.items import JobSamecityItem


class A58jobSpider(Spider):
    name = '58job'
    allowed_domains = ['https://cn.58.com/job']
    start_urls = ['https://cn.58.com/job/pn1']

    def parse(self, response):
        #print(response.text)
        job_lists=response.xpath('//ul[@id="list_con"]/li')
        #print(job_lists)
        for job_list in job_lists:
            #print(job_list)
            item=JobSamecityItem()
            item['job_name']=job_list.xpath('./div/div/a/span[@class="name"]/text()').extract_first()
            item['job_add']=job_list.xpath('./div/div/a/span[@class="address"]/text()').extract_first()
            item['job_salary']=job_list.xpath('./div/p/text()').extract_first()
            item['job_wel']=job_list.xpath('./div/div/span/text()').extract()
            item['comp_name']=job_list.xpath('./div[2]/div/a/text()').extract_first()
            item['job_cate']=job_list.xpath('./div[2]/p/span[@class="cate"]/text()').extract_first()
            item['job_xueli']=job_list.xpath('./div[2]/p/span[@class="xueli"]/text()').extract_first()
            item['job_jingyan']=job_list.xpath('./div[2]/p/span[@class="jingyan"]/text()').extract_first()
            item['date']=job_list.xpath('./span/text()').extract_first()
            yield item

        next_page_url=response.xpath("//a[@class='next']/@href").extract_first()
        if next_page_url:
            url = response.urljoin(next_page_url)
            yield Request(url=url,callback=self.parse,dont_filter=True)
        else:
            return
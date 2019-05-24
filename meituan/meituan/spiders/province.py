# -*- coding: utf-8 -*-
import json

import scrapy

from meituan.items import ProvinceItem


class ProvinceSpider(scrapy.Spider):
    name = 'province'
    allowed_domains = ['www.meituan.com']
    start_urls = ['http://www.meituan.com/ptapi/getprovincecityinfo/']

    def parse(self, response):
        pro_json=response.text
        print(pro_json)
        pro_data=json.loads(pro_json)
        for i in range(len(pro_data)):
            province_code = pro_data[i]['provinceCode']
            province_name = pro_data[i]['provinceName']
            city_info_list = pro_data[i]['cityInfoList']

            item=ProvinceItem()
            city_num = len(city_info_list)
            for j in range(city_num):
                city_id = city_info_list[j]['id']
                city_name = city_info_list[j]['name']
                city_pinyin = city_info_list[j]['pinyin']
                city_acronym = city_info_list[j]['acronym']
                item['city_id'] = city_id
                item['city_name'] = ''.join(city_name)
                item['city_pinyin'] = ''.join(city_pinyin)
                item['city_acronym'] = ''.join(city_acronym)
                item['city_pro_code'] = ''.join(province_code)
                yield item
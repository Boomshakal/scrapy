# -*- coding: utf-8 -*-
from scrapy import Request,Spider
import json
from weibo.items import WeiboItem
class WeibocnSpider(Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0$since_id=1']

    def parse(self, response):
        messages=json.loads(response.text)
        cards=messages.get('data').get('cards')
        for card in cards:
            mblog=card.get('mblog')
            item = WeiboItem()
            try:
                item['user'] = mblog['user']
                item['text']=mblog['text']
                yield item
            except:
                print(None)
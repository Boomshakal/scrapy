# -*- coding: utf-8 -*-
import json
from urllib.parse import urlencode

from scrapy import  Spider,Request

from aiqiyi.items import CommentsItem


class CommentsSpider(Spider):
    name = 'comments'
    page=3
    content_id= 2054805300 #国风美少年
    #allowed_domains = ['http://sns-comment.iqiyi.com/v3/comment/get_comments.action?']
    start_url = 'https://sns-comment.iqiyi.com/v3/comment/get_comments.action?'
    headers={
            'agent_type': 118,
            'agent_version': '9.11.5',
            'authcookie': 'null',
            'business_type': 17,
            'content_id': content_id,
            'hot_size': 0,
            'last_id': '',
            'page': page,
            'page_size': 20,
            'types': 'time',
            #'callback': 'jsonp_1543836570490_3918'
    }
    def start_requests(self):
        url=self.start_url+urlencode(self.headers)
        yield Request(url=url,callback=self.parse)
    def parse(self, response):
        datas=json.loads(response.text)['data']['comments']
        for data in datas:
            item=CommentsItem()
            item['content']=data['content']
            item['addtime']=data['addTime']

            item['gender']=data['userInfo']['gender']
            item['uname']=data['userInfo']['uname']
            item['uid']=data['userInfo']['uid']
            item['uidType']=data['userInfo']['uidType']
            yield item


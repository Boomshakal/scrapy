# -*- coding: utf-8 -*-
from urllib.parse import urlsplit
from scrapy import Request, Spider
import json
from weibo.items import AccountItem, UserItem


class WeibocnSpider(Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    start_id = '3057179881'
    fans_head = '231051_-_fans_-_'
    followers_head = '231051_-_followers_-_'
    user_head = '230283{id}_-_INFO'
    since_id = 2
    page = 2

    user_url = 'https://m.weibo.cn/api/container/getIndex?containerid=' + user_head + '&title=%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99'

    fans_url = 'https://m.weibo.cn/api/container/getIndex?containerid={containerid}&since_id={since_id}'

    followers_url = 'https://m.weibo.cn/api/container/getIndex?containerid={containerid}&page={page}'

    #
    def start_requests(self):
        yield Request(url=self.fans_url.format(containerid=self.fans_head + self.start_id, since_id=self.since_id),
                      callback=self.parse_fans)
        yield Request(url=self.followers_url.format(containerid=self.followers_head + self.start_id, page=self.page),
                      callback=self.parse_followers)

    def parse_followers(self, response):
        result = json.loads(response.text)
        cards = result.get('data').get('cards')[0].get('card_group')
        nexturl_info = result.get('data').get('cardlistInfo')
        containerid = nexturl_info.get('containerid')
        page = nexturl_info.get('page')
        for card in cards:
            id = card.get('user').get('id')
            # print(id)
            yield Request(url=self.user_url.format(id=id), callback=self.parse_user)

        # nextpage
        yield Request(url=self.followers_url.format(containerid=containerid, page=page), callback=self.parse_followers)

    def parse_fans(self, response):

        result = json.loads(response.text)
        cards = result.get('data').get('cards')[0]
        if cards:
            cards=cards.get('card_group')
        # print(cards)
        nexturl_info = result.get('data').get('cardlistInfo')
        containerid = nexturl_info.get('containerid')
        since_id = nexturl_info.get('since_id')
        for card in cards:
            id = card.get('user').get('id')
            # print(id)
            yield Request(url=self.user_url.format(id=id), callback=self.parse_user)

        yield Request(url=self.fans_url.format(containerid=containerid, since_id=since_id), callback=self.parse_fans)

    def parse_user(self, response):
        # print(response.text)
        result = json.loads(response.text)
        id = urlsplit(response.url)[3][18:28]
        # print(id)
        account_info = result.get('data').get('cards')[0].get('card_group')
        user_info = result.get('data').get('cards')[1].get('card_group')
        # print(account_info[2]['actionlog'].get('fid'))
        try:
            account = AccountItem()
            account['id'] = id
            account['nickname'] = account_info[1]['item_content']
            account['weiboauth'] = account_info[2]['item_content']
            account['profile'] = account_info[3]['item_content']
            # account['level']=account_info[4]['item_content']
            # account['creat_time']=account_info[5]['item_content']
            # account['sun_credit']=account_info[6]['item_content']

            user = UserItem()
            user['head_id'] = id
            user['gender'] = user_info[1]['item_content']
            user['location'] = user_info[2]['item_content']

            yield account
            yield user

        except:
            print(None)

        yield Request(url=self.fans_url.format(containerid=self.fans_head + id, since_id=self.since_id),
                      callback=self.parse_fans)
        yield Request(url=self.followers_url.format(containerid=self.followers_head + id, page=self.page),
                      callback=self.parse_followers)

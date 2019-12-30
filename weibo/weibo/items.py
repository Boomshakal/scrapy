# -*- coding= utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in=
# https=//doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AccountItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    id = Field()
    nickname = Field()  # 昵称
    weiboauth = Field()  # 微博认证
    profile = Field()  # 简介
    level = Field()  # 等级
    creat_time = Field()  # 注册时间
    sun_credit = Field()


class UserItem(Item):
    head_id = Field()
    gender = Field()
    birthday = Field()
    location = Field()

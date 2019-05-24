# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class MeituanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProvinceItem(Item):
    city_pro_code = Field()
    city_id = Field()
    city_name = Field()
    city_pinyin = Field()
    city_acronym = Field()


class MeiShi(Item):
    avgPrice = Field()
    avgScore = Field()
    cateName = Field()
    channel = Field()
    frontImg = Field()
    lat = Field()
    lng = Field()
    name = Field()
    poiid = Field()
    areaName = Field()
    ctPoi = Field()
    adress = Field()
    phone = Field()
    openinfo = Field()
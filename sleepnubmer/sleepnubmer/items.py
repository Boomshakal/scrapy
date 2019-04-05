# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class SleepnubmerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title=Field()
    address_info=Field()
    city=Field()
    abbr=Field()
    post=Field()
    phone=Field()



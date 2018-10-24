# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class TejiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    all_order=Field()
    category=Field()
    coupon_end_time=Field()
    coupon_money=Field()
    coupon_price=Field()
    coupon_start_time=Field()
    datasource=Field()
    discount=Field()
    doc_id=Field()
    id=Field()
    is_top=Field()
    lastofftime=Field()
    new_commission_rate=Field()
    pic_url=Field()
    price=Field()
    priceType=Field()
    quan_recieve=Field()
    quan_surplus=Field()
    sale_total=Field()
    sale_url=Field()
    salecount=Field()
    shop_type=Field()
    site_id=Field()
    title=Field()
    update_time=Field()
    v_order=Field()

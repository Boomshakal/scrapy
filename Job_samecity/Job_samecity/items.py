# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Field,Item


class JobSamecityItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name=Field()
    job_add=Field()
    job_salary=Field()
    job_wel=Field()
    comp_name=Field()
    job_cate=Field()
    job_xueli=Field()
    job_jingyan=Field()
    date=Field()



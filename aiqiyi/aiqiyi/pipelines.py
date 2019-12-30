# -*- coding: utf-8 -*-
import time
import pymongo
from aiqiyi.items import CommentsItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TimePipeline(object):
    def process_item(self, item, spider):
        timeArray = time.localtime(item['addtime'])#秒数
        item['addtime']=time.strftime("%Y-%m-%d %H:%M:%S",timeArray)
        return item

class GenderPipeline(object):
    def process_item(self, item, spider):
        if item['gender']=='0':
            item['gender']='女'
        elif item['gender']=='1':
            item['gender']='男'
        return item


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'comments')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        # self.client = pymongo.MongoClient("mongodb://root:root@192.168.234.129/aiqiyi")
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection_name = item.__class__.__name__
        self.db[collection_name].insert(dict(item))
        return item

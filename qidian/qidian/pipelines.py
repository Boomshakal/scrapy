# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class QidianPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveTextPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        print(base_dir)
        fiename = base_dir + '/小说.txt'
        with open(fiename, "a",encoding='utf-8') as f:
            f.write(item['chaptername'] + "\n")
            for content in item['content']:
                f.write(content +"\n\n")
        return item
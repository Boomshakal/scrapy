# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from meizitu.settings import IMAGES_STORE


class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item




class PhotoPipeline(object):
    def process_item(self, item, spider):
        images=[]
        dir_path = '{}'.format(IMAGES_STORE)
        header = {
            'referer': item['src'],
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1555902619,1555908635,1555908883,1555910146; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1555910416'
            # 需要查看图片的cookie信息，否则下载的图片无法查看
        }
        #print(item)
        jpg_url=item['src']
        file_name = item['title']
        file_path = '{}//{}'.format(dir_path, file_name)
        images.append(file_path)
        if os.path.exists(file_path) or os.path.exists(file_name):
            return
        with open('{}//{}.jpg'.format(dir_path, file_name), 'wb') as f:
            req = requests.get(jpg_url, headers=header)
            f.write(req.content)
        return item
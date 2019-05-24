# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware

from qidian.settings import COOKIES





class RandomCookieMiddleware(CookiesMiddleware):
    '''
    随机cookie池
    '''
    def process_request(self, request, spider):
        cookie = random.choice(COOKIES)
        request.cookies = cookie

# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json

import requests
from scrapy import signals

import time
import random


from scrapy.downloadermiddlewares.cookies import CookiesMiddleware
from scrapy.http import HtmlResponse

from zhilian.settings import COOKIES


class RandomCookieMiddleware(CookiesMiddleware):
    '''
    随机cookie池
    '''
    def process_request(self, request, spider):
        cookie = random.choice(COOKIES)
        request.cookies = cookie


class PayLoadRequestMiddleware:
    def process_request(self, request, spider):
        # 如果有的请求是带有payload请求的，在这个里面处理掉
        if request.meta.get('payloadFlag', False):
            print(f"PayLoadRequestMiddleware enter")
            postUrl = request.url
            headers = request.meta.get('headers', {})
            payloadData = request.meta.get('payloadData', {})
            proxy = request.meta['proxy']
            proxies = {
                "http": proxy,
                "https": proxy,
            }
            timeOut = request.meta.get('download_timeout', 25)
            allow_redirects = request.meta.get('dont_redirect', False)
            dumpJsonData = json.dumps(payloadData)
            print(f"dumpJsonData = {dumpJsonData}")
            # 发现这个居然是个同步 阻塞的过程，太过影响速度了
            res = requests.post(postUrl, data=dumpJsonData, headers=headers, timeout=timeOut, proxies=proxies, allow_redirects=allow_redirects)
            # res = requests.post(postUrl, json=payloadData, headers=header)
            print(f"responseTime = {time.time()}, res text = {res.text}, statusCode = {res.status_code}")
            if res.status_code > 199 and res.status_code < 300:
                # 返回Response，就进入callback函数处理，不会再去下载这个请求
                return HtmlResponse(url=request.url,
                                    body=res.content,
                                    request=request,
                                    # 最好根据网页的具体编码而定
                                    encoding='utf-8',
                                    status=200)
            else:
                print(f"request mode getting page error, Exception = {e}")
                return HtmlResponse(url=request.url, status=500, request=request)
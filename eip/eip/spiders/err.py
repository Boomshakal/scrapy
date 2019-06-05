# -*- coding: utf-8 -*-
import re

import execjs
import requests
import time
from scrapy import FormRequest,Spider,Request


class ErrSpider(Spider):
    name = 'err'
    #allowed_domains = ['http://eip.megmeet.com:8008/']
    start_urls = ['http://eip.megmeet.com:8008/sys/portal/page.jsp']
    longin_url = "http://eip.megmeet.com:8008/j_acegi_security_check/"

    time = int(time.time()*1000)
    url = 'http://eip.megmeet.com:8008/resource/js/session.jsp?_={time}&s_ajax=true'

    result = requests.get(url=url.format(time=time))
    sessionid = re.findall('return "(.*?)"', result.text)[0]

    passwd = execjs.compile(open(u"eip/EIP.js").read()).call('desEncrypt', '******', sessionid)
    # print(passwd)
    def start_requests(self):
        yield Request(url=self.longin_url, callback = self.post_login)

    def post_login(self, response):
        yield FormRequest.from_response(
            response,
            formdata={
                'j_username' : '******',
                'j_password' : self.passwd,
                'j_lang': 'zh - CN',
                'j_redirectto': 'http://eip.megmeet.com:8008/index.jsp',
            },
            callback=self.parse
            )

    def parse(self, response):
        print(response.text)

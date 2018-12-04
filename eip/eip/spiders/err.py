# -*- coding: utf-8 -*-

from scrapy import FormRequest,Spider,Request


class ErrSpider(Spider):
    name = 'err'
    #allowed_domains = ['http://eip.megmeet.com:8008/']
    start_urls = ['http://eip.megmeet.com:8008/sys/portal/page.jsp']
    longin_url = "http://eip.megmeet.com:8008/j_acegi_security_check/"

    # username = input("请输入账号：")
    # password = input("请输入密码：")
    def parse(self, response):
        yield FormRequest.from_response(
            response,  # 传入response对象,自动解析
            # 可以通过xpath来定位form表单,当前页只有一个form表单时,将会自动定位
            formdata={"j_username": 'yhs375', "j_password": '䐵匠䴵GIjAUOsc9UEZ4FRqcQhk1w==','j_redirectto': 'http://eip.megmeet.com:8008/index.jsp'},
            callback=self.parse_login,
        )

    def parse_login(self, response):

        print(response.text)




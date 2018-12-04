#!/usr/bin/python
# -*- coding: UTF-8 -*-

import execjs,os
#执行本地自定义的js
print (execjs.compile('function test(){'
               'return 5'
               '}'
               ''
               ''
               '').call("test"))
import re

import execjs
import requests
import time
time=int(time.time()*1000)
# a='1559703644059'
url = 'http://eip.megmeet.com:8008/resource/js/session.jsp?_={time}'.format(time=time)
result = requests.get(url=url)
sessionid=re.findall('return "(.*?)"',result.text)[0]

passwd=execjs.compile(open(u"EIP.js").read()).call('desEncrypt','lhm922357',sessionid)
print(passwd)
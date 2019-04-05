from urllib.parse import urlsplit
url='https://m.weibo.cn/p/index?containerid=2302833942929375_-_INFO&title=%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99'

result=urlsplit(url)
print(result[3][18:28])
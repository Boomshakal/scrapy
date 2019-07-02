from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')

# print(scrapyd.list_jobs('zhihuuser'))

# print(scrapyd.list_spiders('zhihuuser'))

# scrapyd.schedule('zhihuuser', 'zhihu')


# 取消job
print(scrapyd.cancel('zhihuuser', '3c67450e9ccc11e98f7894659c699c36'))
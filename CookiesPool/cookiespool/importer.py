import requests

from cookiespool.db import RedisClient

website = input('输入网站域名：')   #website 如 weibo
conn = RedisClient('accounts', website)

def set(account, sep=','):
    username, password = account.split(sep)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入'+website+'账号密码组, 输入exit退出读入')
    while True:
        account = input()
        if account == 'exit':
            break
        set(account)


if __name__ == '__main__':
    scan()
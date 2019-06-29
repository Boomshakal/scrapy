import requests
from proxypool.setting import TEST_URL
from bs4 import BeautifulSoup

def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    proxy = BeautifulSoup(r.text, "lxml").get_text()
    return proxy


def crawl(url, proxy):
    proxies = {'http': proxy}
    r = requests.get(url, proxies=proxies)
    return r.text

proxy = get_proxy()

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
print(proxies)
print(TEST_URL)
response = requests.get(TEST_URL, proxies=proxies, verify=False)
if response.status_code == 200:
    print('Successfully')
    print(response.text)
import requests
from bs4 import BeautifulSoup

def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    proxy = BeautifulSoup(r.text, "lxml").get_text()
    return proxy


def crawl(url, proxy):
    proxies = {'http': proxy}
    r = requests.get(url, proxies=proxies)
    return r.text




def location(address):
    url='https://www.latlong.net/_spm4.php'
    data={
        'c1': address,
        'action': 'gpcm'
    }
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }



    result=requests.post(url=url,data=data,headers=headers).text  #verify是否验证服务器的SSL证书
    return result


if __name__ == '__main__':

    # a=location('Alabama')
    # print(a)
    b=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusettes','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New York','New Mexico','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennslyvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    for i in b:
        print(location(i))
#'https://www.sleepnumber.com/api/1/find-mattress-stores?latitude=40.712776&longitude=-74.005974'



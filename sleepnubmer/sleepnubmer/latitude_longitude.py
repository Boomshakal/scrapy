import requests

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
    result=requests.post(url=url,data=data,headers=headers).text
    return result

if __name__ == '__main__':

    a=location('New York')
    print(a.split(',')[0])
    b=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusettes','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New York','New Mexico','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennslyvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    print(len(b))
#'https://www.sleepnumber.com/api/1/find-mattress-stores?latitude=40.712776&longitude=-74.005974'



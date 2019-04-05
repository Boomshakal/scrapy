import re

import requests
from bs4 import BeautifulSoup


def number(url):
    info=open('info.txt','r').read()
    info = info.split('.')
    numbers=get_numbers(url)
    #print(sum(len(i) for i in numbers))
    changedic,w,j,p,q= {},'',0,0,0
    data,row,col={},[],[]

    for i in info:
        w = w + i
        if j == 3:
                 if 'mva' in w :
                    data[re.findall(r'px -(.*?)px', w)[0]+'/'+re.findall(r'background:-(.*?)px', w)[0]] = w.split('{')[0]
                    col.append(re.findall(r'background:-(.*?)px', w)[0])
                    row.append(re.findall(r'px -(.*?)px', w)[0])
                 w ,j= '',0
        j = j + 1
    #print(data)
    row=set(row)
    rows = [int(i) for i in row]
    #print(rows)
    #print(len(rows),len(numbers))
    col = set(col)
    cols = [int(i) for i in col]
    #print(cols)
    result = {}
    for i,j in zip(sorted(rows),range(len(numbers))):
        t = numbers[j]
        p=0
        for q in sorted(cols):
            key = str(i) + '/' + str(q)
            try:
                result['<span class="{0}"></span>'.format(data[key])] = t[p]
                p+=1

            except :
                continue
    #print(len(result))
    return result

def chinese(url):
    info=open('info.txt','r').read()
    info = info.split('.')
    text=get_chinese(url)
    #print(text)
    #print(sum(len(i) for i in text))  #共有多少字
    w,j,s,data,col,row='',0,[],{},[],[]
    for i in info:
        w = w + i
        if j == 3:
            if 'tnq' in w :
                s.append(w)
                data[re.findall(r'px -(.*?)px', w)[0]+'/'+re.findall(r'background:-(.*?)px', w)[0]] = w.split('{')[0]
                col.append(re.findall(r'background:-(.*?)px', w)[0])
                row.append(re.findall(r'px -(.*?)px', w)[0])
            w ,j = '',0
        j = j + 1
    print(data)
    row = set(row)
    rows = [int(i) for i in row]
    #print(len(rows))
    print(rows,len(rows),len(text))
    col = set(col)
    cols = [int(i) for i in col]
    #print(cols,len(cols))
    result = {}
    for i, j in zip(sorted(rows), range(len(text))):
        #print(i,j)
        t = text[j]
        p = 0
        for q in sorted(cols):
            key = str(i) + '/' + str(q)
            #print(key)
            try:
                result['<span class="{0}"></span>'.format(data[key])] = t[p]
                p += 1

            except:
                continue
    result['<br/>']='。'
    result['\xa0']='；'
    #print(len(result))
    return result

def get_chinese(url):
    text=[]
    #url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/206f3442312ce0a851b0d0b06dc58368.svg'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    soup = soup.find_all('textpath')
    for i in soup:
        text.append(i.text)
    return text
def get_numbers(url):
    numbers=[]
    #url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/50afb6ac9bcd894c3f260cda3e0ad6e2.svg'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    soup = soup.find_all('text')
    for i in soup:
        numbers.append(i.text)
    return numbers

if __name__ == '__main__':
    # a=number()
    # print(a['<span class="mvao2i"></span>'])
    url_number='http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/50afb6ac9bcd894c3f260cda3e0ad6e2.svg'
    url_chinese='http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/bccbe0abb06ce0d2e79dcd81aaeb118e.svg'
    number=number(url_number)
    text=chinese(url_chinese)

    print(number['<span class="mva61q"></span>'])
    print(text['<span class="tnqx5k"></span>'])

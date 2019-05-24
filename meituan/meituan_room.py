'''
author: Andy丶Tao
csdn博客: https://blog.csdn.net/tao15716645708
'''

import requests, zlib, base64
import random, re
import json, jsonpath
#import pymysql
from datetime import datetime
from bs4 import BeautifulSoup


def getTime():
    '''
    :return: 返回从1970.1.1至今的毫秒数
    '''
    d1 = datetime(1970, 1, 1)
    d2 = datetime.now()
    d3 = int((d2 - d1).total_seconds() * 1000)
    return d3


def url_encode(data, stringify=False):
    '''
    token编码
    :param data: 编码参数
    :param stringify: boolean,默认序列化
    :return: token编码
    '''
    if (stringify == True):
        base_data = zlib.compress(data.encode())
        data = base64.b64encode(base_data)
        return data
    else:
        data = json.dumps(data).replace(' ', "")
        return url_encode(data, True)


def url_decode(data):
    """token解码"""
    if isinstance(data, str):
        data = base64.b64decode(data)
        base_data = zlib.decompress(data)
        return base_data


def get_taken(url):
    '''
    访问酒店链接，从响应体里得到需要的参数信息
    :param url: url
    :return: taken
    '''
    cookies_iuuid = [
        '93AB5D4FEB3D1BFFF9B7727E5ECE71CF13A51383CD6ADB169C43832A6BB41843',
        '8A8E20A923D42E033BC3505E3460BCC25AEA4D933CE3F233B19679BB0EEC89D4',
        'C68174784AF5C11CC2F127774CC8BA60FB5E766509A7DCA8F4ECDFF59B45076F',
        '850C1A14A798DC5834EEF2177EAAA430A8958DBE0813C5FAE858B61834D1F95D'
    ]
    response = requests.get(url, headers=headers, timeout=2.0)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    taken = {}
    taken["name"] = soup.select('.fs26.fc3.pull-left.bold')[0].text
    taken["cityId"] = re.findall(r'"cityId":[0-9]*', response.text)[0][8:]
    taken["poiId"] = re.findall(r'"poiId":[0-9]*', response.text)[0][8:]
    taken["start"] = re.findall(r'"queryStart":[0-9]*', response.text)[0][13:]
    taken["end"] = re.findall(r'"queryEnd":[0-9]*', response.text)[0][11:]
    taken["?type"] = "1"
    taken["&utm_medium"] = "PC"
    taken["version_name"] = "7.3.0"
    # taken["uuid"] = cookies_iuuid[random.randint(0,3)]
    taken["uuid"] = '7B20F54E2E3033B75A6B3775DDFDDF7D8EB12B67BA73BF1FA0FAB35619FDE640'  # 如果这个uuid不管用，就把该行注释，并打开上一行注释
    return taken


def get_tokon(taken):
    '''
    生成sign的值，并得到_token字典
    :param taken: 明参
    :return: _tokon
    '''
    sign = '"end=%s&poiId=%s&start=%s&type=1&utm_medium=PC&uuid=%s&version_name=%s"' % (
        taken['end'], taken['poiId'], taken['start'], taken['uuid'], taken['version_name'])
    _tokon = {
        "rId": 100051,
        "ts": getTime(),
        "cts": getTime() + 356,
        "brVD": [1536, 222],
        "brR": [[1536, 864], [1536, 824], 24, 24],
        "bI": ["%s" % url, ""],
        "mT": [],
        "kT": [],
        "aT": [],
        "tT": [],
        "sign": url_encode(sign).decode()
    }
    return _tokon


def get_url(_url):
    '''
    由于url连接各式各样，这里提取id，并拼接为一个最简洁的url
    :param _url:
    :return:
    '''
    url = re.findall(r'(.*?)(\d+\.?\d*)', _url)
    return url[0][0] + url[0][1]


def get_service(all_introduce_introduce):
    '''
    service detail
    :param all_introduce_introduce:
    :return:
    '''
    if len(all_introduce_introduce) == 3:
        [area, bed, window] = all_introduce_introduce
        return area, bed, window
    if len(all_introduce_introduce) == 2:
        [bed, window] = all_introduce_introduce
        area = ''
        return area, bed, window
    if len(all_introduce_introduce) == 1:
        [window] = all_introduce_introduce
        area, bed = '', ''
        return area, bed, window


def get_idPriceDict(room_type_list):
    '''
    得到全部结果。
    想要看一步一步得出的结果是什么，只需要把各个注释打开打印出来看一下就一目了然
    :param room_type_list:
    :return:
    '''
    # bathroom = '独立'
    for room_type in room_type_list:
        # all_introduce_roomName = room_type['roomCellName']
        # all_introduce_roomPrice = room_type['lowestPrice']
        all_introduce_introduce = room_type['roomCellDesc'].split('|')
        area, bed, window = get_service(all_introduce_introduce)
        # print(all_introduce_roomName, area, bed, window, all_introduce_roomPrice)
        _detail = room_type['aggregateGoods']
        for detail in _detail:
            # print(detail)
            try:
                room_name = detail['prepayGood']['goodsRoomModel']['roomName']
            except:
                continue
            price = int(int(detail['prepayGood']['averagePrice']) / 100)
            breakfast = detail['prepayGood']['breakfast']
            _time = str(datetime.now())[0:10]
            ota_name = taken["name"]
            print(ota_name, room_name, area, bed, window, breakfast, price, _time)
            # sql_insrt(ota_name, room_name, area, bed, window, breakfast, price, _time)  # 如需存入数据库， 请打开该行注释


# def sql_insrt(ota_name, room_name, area, bed, window, breakfast, price, _time):
#     try:
#         _insert = ""  # insert 语句
#         cursor.execute(_insert)
#         conn.commit()
#     except:
#         conn.rollback()


def spider(data_url, taken):
    '''
    spider
    :param data_url:
    :param taken:
    :return:
    '''
    response = requests.get(data_url, headers=headers).text
    response_jsonObj = json.loads(response)
    # name = taken['name']  # 如需要得到酒店名字，把改行注释去掉就ok
    room_type_list = jsonpath.jsonpath(response_jsonObj, '$.mergeList.data')[0]
    id_data_list = jsonpath.jsonpath(response_jsonObj, '$.propagateData')[0]
    get_idPriceDict(room_type_list)


if __name__ == '__main__':
    url_list = ['']  # 这里传入美团url列表
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
    # 如需存入数据库请打开一下两行注释
    # conn = pymysql.connect(host='***', port=3306, user='***', password='***', db='***')  # 这里填写你的数据库信息
    # cursor = conn.cursor()
    for index, _url in enumerate(url_list):
        url = get_url(_url)
        taken = get_taken(url)

        _tokon = get_tokon(taken)
        __token = url_encode(
            _tokon).decode()  # 将_token字典加密得到之前文章所讲的_token参数，拼接这些参数，得到下一行的数据接口url   文章传送门：https://blog.csdn.net/tao15716645708/article/details/82970423
        data_url = "https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=" + \
                   taken["poiId"] + "&start=" + taken["start"] + "&end=" + taken["end"] + "&uuid=" + taken[
                       "uuid"] + "&_token=" + __token + '&X-FOR-WITH=ssc099pw7M1pSLnctp7N0kxDTVNn%2BVh0oQz3qqhb%2FjnrLHQUHnKqegSbhjHF3%2B%2B2iOGshjOzGUmqUFgeGrVNdJEeSCp88LRyhmpaR77ddhNhNoBKnCikirKGUUj%2FdaWfmjFa6p8NWz4EdtbRzkbhgA%3D%3D'
        spider(data_url, taken)  # 爬虫主程序
        # break

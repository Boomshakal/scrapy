import json

import requests

url = 'https://apiapp.zhaopin.com/ihrapi/resume/getrecommendresumelist?access_token=96cfae7d73564f5b8f7762fa2f8bb833&pageSize=20&pageIndex=20&jobNumber=CC252722022J00349923303'
headers = {
    'Host': 'apiapp.zhaopin.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'x-zp-client-id=be2de5ef-563b-4006-acb4-f73ecd427a87; sts_deviceid=16b4eca972d5d6-057f59ed9271b1-e353165-1638720-16b4eca972f516; __utmz=269921210.1560395028.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); urlfrom2=121113803; adfbid2=0; NTKF_T2D_CLIENTID=guest8DCEC7C1-BD7E-64E2-4969-4ECB5268176C; diagnosis=0; hideAnnounceNotify=1; x-zp-device-id=f4264ba02915e01489f56d351dbca5ef; __utma=269921210.1727489822.1560395028.1560412717.1561423366.3; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1561423376; JSloginnamecookie=15168633879; JSShowname=""; JSpUserInfo=36672168546b5a754177577144654371546355655869586b4c714c653d772b774c6552675068586b5d7549775371446544715d6350655169506b30713a654c77097718650b671068006b067518770b71066506712563006505690a6b1c711b655f7706771e650e675e683a6b3f754c7754714c65367131635a655d69466b4771576549775f77456557675e68286b27754c7754714c65227124635a652269226b4771446545775477436553675668506b5f754a77307123654a7154635c653b69226b487147654a77307721652d675868066b057546771771066543710b63176512691b6b01711d6516770377156512675668116b0e75497710710f651471016354651169026b1c714c651; uiioit=213671340f69446b5d6a5a7947644774073506325975586d5368427426733036083402694e6b8; zp-route-meta=uid=132787351,orgid=25272202; login_point=25272202; promoteGray=; urlfrom=121113803; adfbid=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22132787351%22%2C%22%24device_id%22%3A%2216b4eca95c314c-0f6919a300b3ad-e353165-1638720-16b4eca95c474%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsj_Iw7I00000r2_AdC00000X8254C.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15ymsPvDsPj6Lnj0sPjRknyc0IHYLnYw7PDNAn1T1nHf3nDRdfYmdrjb%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%2216b4eca95c314c-0f6919a300b3ad-e353165-1638720-16b4eca95c474%22%7D; sts_sg=1; sts_sid=16b8c34fd75343-064bef402a52e5-e343166-1638720-16b8c34fd772aa; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsj_Iw7I00000r2_AdC00000X8254C.THLyktAJdIjA80K85yF9pywdpAqVuNqsusK15ymsPvDsPj6Lnj0sPjRknyc0IHYLnYw7PDNAn1T1nHf3nDRdfYmdrjb1PbmswDfsPYRknsK95gTqFhdWpyfqn1cznWmzPH63PBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1YYnjcYPs%26tpl%3Dtpl_11535_18778_14772%26l%3D1511763170%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3222625886_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D241%26ie%3Dutf-8%26f%3D3%26tn%3Dbaiduhome_pg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26inputT%3D5012; dywea=95841923.3887055483229229000.1560395028.1561423365.1561425472.5; dywec=95841923; dywez=95841923.1561425472.5.2.dywecsr=landing.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/register; __utmc=269921210; __utmt=1; at=fffc4902af7b4a698cd2ba2f5413b1a5; rt=44048e9d864945e3a48cb787019c1eb8; login-type=b; nTalk_CACHE_DATA={uid:kf_9051_ISME9754_25272202,tid:1561425545601132}; sts_evtseq=2; __utmb=269921210.15.10.1561423366; dyweb=95841923.2.10.1561425472'
}
result = requests.get(url=url, headers=headers)

# print(result.text)
datas = json.loads(result.text)['data']['recommendResumes']
# print(len(datas))
info = {}
for data in datas:
    info['tel'] = '***'
    info['sex'] = str(data['genderKey'])
    info['label_name'] = data['jobTitle']
    info['head_pic_path'] = data['photoUrl']
    info['name'] = data['userName']
    info['address'] = data['cityName']
    info['work_years'] = str(data['workYear'])

    if data['educationLabels'] != []:
        info['education'] = str(data['educationLabels'][0]['name'])
    else:
        info['education'] = ''
    info['work_path'] = ''
    info['introduce'] = ''
    info['education_experience'] = str(i for i in data['educationExperiences'])
    info['project_experience'] = ''
    info['work_experience'] = str(data['workExperiences'])
    if data['desireWorkSalaryRange'] != '面议':

        salary_start, salary_end = data['desireWorkSalaryRange'].split('-')
        if salary_start.endswith('千'):
            salary_start = float(salary_start[:-1]) * 1000
        elif salary_start.endswith('万'):
            salary_start = float(salary_start[:-1]) * 10000
        if salary_end.endswith('千'):
            salary_end = float(salary_end[:-1]) * 1000
        elif salary_end.endswith('万'):
            salary_end = float(salary_end[:-1]) * 10000
    else:
        salary_start, salary_end = 0, 0
    info['salary_start'] = salary_start
    info['salary_end'] = salary_end
    info['for_id'] = data['userMasterId']
    info['other_info'] = ''

    # print(info)

    # post数据
    info_json = json.dumps(info, ensure_ascii=False)
    # print(info_json)
    url = 'https://cs.woheyun.com/api/cgwas/otherUser/create.json?data={}'.format(info_json)
    # print(url)
    status = requests.get(url)
    print(status.text)
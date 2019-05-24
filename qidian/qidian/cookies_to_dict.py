import random




def cookieChangeToDict(cookie):
    '''
    将cookie字符串转换成字典
    :param cookie: 登录后的cookie
    :return:字典
    '''
    cookieList = cookie.split(';')
    cookieDict = {}
    for cookie in cookieList:
        name = cookie.split('=', maxsplit=1)[0].strip()
        value = cookie.split('=', maxsplit=1)[1].strip()
        cookieDict[name] = value
    return cookieDict

if __name__ == '__main__':
    cookie = """e1=%7B%22pid%22%3A%22qd_P_read%22%2C%22eid%22%3A%22%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_P_read%22%2C%22eid%22%3A%22qd_R120%22%2C%22l1%22%3A3%7D; _csrfToken=WvQsm26pWYfiIjKFbLQ45Sr0jG2XR87L3oXAp7JH; newstatisticUUID=1558593284_547639355; e1=%7B%22pid%22%3A%22qd_P_Searchresult%22%2C%22eid%22%3A%22qd_S05%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_H_Search%22%2C%22l1%22%3A2%7D; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1; rcr=1013520024; bc=1013520024; lrbc=1013520024%7C465418969%7C0; ywkey=yw43N3F4Z6LU; ywguid=2047114221; ywopenid=35EAB25AF84151FD18D31F67D4ACED98; pgv_pvi=9700907008; pgv_si=s5596383232; _qddaz=QD.9infzg.ukc61c.jw0b5106
    """
    print(cookieChangeToDict(cookie))

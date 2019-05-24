# import pymongo
#
# conn=pymongo.MongoClient('localhost',27017)
# db=conn.meituan
# table=db.ProvinceItem
# #print(table)
# for i in table.find():
#     print(i)

import base64, zlib
token='eJxVjktvqkAYhv/LbCUyjDAMJl3AgeMFQQuI1MYF4CDUchFGqJyc/95p0i6afMl7+Z7F+w+0qzOYSxBqEAqgpy2YA2kKpxgIgHX8oyiyhjFUCZI0AaS/u5ksCyBpQxPMXwlGAoHK6avweH5FUCaCJCnoJPx4iZwEJPP7olYcAjljzVwUu3Fa0oLd42qa1qXIfZcXYoKIyHcATpcBp7levzX+VvaTHT6cs11xqbij6yF827Ot8cfae1nmX0Zq1ffWC47XwTHhw0mVVNc3YeAPk8sLXbdd6C50evfdNM/2aeWK59FxD4mBz5Vxjp+Xo2+YWTA52psoG7WsV8RMttZ23yhjMPN2oZUu0pv1TEdWKepBjxznvdlSjB/Mu9MtyRKz1meHoHSQZyI1Gv5q5Ue8eHlgyQ/s/cetC0m+WSWost0B47wPVOyqZJe0pZ8zlajR0tCii1/oPVw246KmyBqL28Y244rlh+PVWEdb/9qgdFW6+Wyi861+WT+B/59wNpDO'
token_decode = base64.b64decode(token.encode()) # token为token字符串

# 解压16进制数据流
token_string = zlib.compress(token_decode)
print(token_string)
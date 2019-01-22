import execjs


jiamipasswd=execjs.compile(open(r"111.js").read()).call('add',1,2)
print(jiamipasswd)

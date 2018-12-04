import time
timeArray = time.localtime(1543835900)#秒数
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
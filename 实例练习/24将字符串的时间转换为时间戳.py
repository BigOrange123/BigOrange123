#coding=gbk
'''将字符串的时间转换为时间戳'''
import time
print(time.time()) # time()获取当前时间戳
print(time.localtime()) # localtime()获取当前时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) #strftime()把时间元组转换成固定格式时间字符串


a1 = "2019-5-10 23:40:00"
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S") # 把固定时间字符串先转换为时间元组
# print(timeArray)
print(int(time.mktime(timeArray))) # mktime()把时间元组转换成时间戳

timeStamp = 1557502800
timeArray = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timeStamp))
print(timeArray)
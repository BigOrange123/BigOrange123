# coding=gbk
'''获取昨天日期'''
# 引入日期模块
import datetime
def getYesterday():
    today = datetime.date.today() # 获取当前时间
    oneday = datetime.timedelta(days=1) # 获取一天时间
    yesterday = today - oneday
    return yesterday

print("昨天日期：{0}".format(getYesterday()))

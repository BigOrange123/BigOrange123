#coding=gbk
'''获取某月日历'''
import calendar
cal = calendar.month(2020,6)
calLen = calendar.monthlen(2020,6)
print(cal)
print(calLen)

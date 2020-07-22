# coding=gbk
'''计算每个月天数'''
'''
    monthrange:输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数
    0:星期一
    1:星期二
    2:星期三
    3:星期四
    4:星期五
    5:星期六
    6:星期
    monthlen:指定月天数
'''
import calendar
month = calendar.monthrange(2020,6)
month1 = calendar.monthlen(2020,6)
print(month,month1)
print(calendar.mdays)
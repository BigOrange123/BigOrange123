# coding=gbk
'''��ȡ��������'''
# ��������ģ��
import datetime
def getYesterday():
    today = datetime.date.today() # ��ȡ��ǰʱ��
    oneday = datetime.timedelta(days=1) # ��ȡһ��ʱ��
    yesterday = today - oneday
    return yesterday

print("�������ڣ�{0}".format(getYesterday()))

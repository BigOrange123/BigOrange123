#coding=gbk
'''���ַ�����ʱ��ת��Ϊʱ���'''
import time
print(time.time()) # time()��ȡ��ǰʱ���
print(time.localtime()) # localtime()��ȡ��ǰʱ��Ԫ��
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) #strftime()��ʱ��Ԫ��ת���ɹ̶���ʽʱ���ַ���


a1 = "2019-5-10 23:40:00"
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S") # �ѹ̶�ʱ���ַ�����ת��Ϊʱ��Ԫ��
# print(timeArray)
print(int(time.mktime(timeArray))) # mktime()��ʱ��Ԫ��ת����ʱ���

timeStamp = 1557502800
timeArray = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timeStamp))
print(timeArray)
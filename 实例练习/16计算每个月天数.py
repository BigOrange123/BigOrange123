# coding=gbk
'''����ÿ��������'''
'''
    monthrange:�������һ��Ԫ�飬��һ��Ԫ���������·ݵĵ�һ���Ӧ�������ڼ���0-6�����ڶ���Ԫ��������µ�����
    0:����һ
    1:���ڶ�
    2:������
    3:������
    4:������
    5:������
    6:����
    monthlen:ָ��������
'''
import calendar
month = calendar.monthrange(2020,6)
month1 = calendar.monthlen(2020,6)
print(month,month1)
print(calendar.mdays)
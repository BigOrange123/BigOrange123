# coding=gbk
'''ʵ�������'''
import time

print('���»س���ʼ��ʱ������ Ctrl + C ֹͣ��ʱ��')
while True:

    input("")  # ����� python 2.x �汾��ʹ�� raw_input()
    starttime = time.time()
    print('��ʼ')
    try:
        while True:
            print('��ʱ: ', round(time.time() - starttime, 0), '��')
            time.sleep(1)
    except KeyboardInterrupt:
        print('����')
        endtime = time.time()
        print('�ܹ���ʱ��Ϊ:', round(endtime - starttime, 2), 'secs')
        break



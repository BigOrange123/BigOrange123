#coding=gbk
'''Լɪ����������С��Ϸ'''
'''
30 ������һ�����ϣ����أ���Ҫ 15 ���´���
���������ų�һ�ӣ��Ŷӵ�λ�ü�Ϊ���ǵı�š�
�������� 1 ��ʼ������ 9 �����´���
���ѭ����ֱ�����Ͻ�ʣ 15 ��Ϊֹ���ʶ�����Щ��ŵ����´����أ�
'''

peopleList = []
for p in range(1,31):
    peopleList.append(p)

def game():
    atuo = 0
    count = 0
    for pl in peopleList:
        atuo+=1
        if atuo == 9:
            atuo = 0
            count +=1
            print(pl)
            # game()
            if count == 15:
                break
game()
print(peopleList)
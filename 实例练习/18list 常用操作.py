# coding=gbk
'''list ���ò���'''
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[2])
print(li[0:3]) # ������Ƭ����ҿ�

# list ����Ԫ��
li.append("new")
print(li)

li.insert(2,"02cheng")
print(li)

li02 = [1,2,3]
li.extend(li02)
print(li)

# list ����
print(li.index("new"))

# list ɾ��Ԫ��
li.remove("new") # ɾ���״γ��ֵ�һ��ֵ
li.pop() # pop ����������: ɾ�� list �����һ��Ԫ��, Ȼ�󷵻�ɾ��Ԫ�ص�ֵ��


# ʹ��join����list��Ϊ�ַ���
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
paramsList = ["%s=%s"%(k,v) for k,v in params.items()]
paramsStr = "&".join(paramsList)
print(paramsStr)

params02 = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
params02List = []
for k,v in params02.items():
    params02List.append(k+"="+v)
params02Str = "&".join(params02List)
print(params02Str)

# list �ָ��ַ���
print(paramsStr.split("&"))

# list ��ӳ�����
list03 = [1,2,3,4]
print([i*2 for i in list03])

# dictionary �еĽ���
dic = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(dic.keys()) # ��ȡ�ֵ������м�
print(dic.values()) # ��ȡ�ֵ�������ֵ
print(["%s=%s"%(k,v) for k,v in dic.items()]) # ���ֵ�����ɼ���

# list ����
li05 = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li05 if len(elem) > 1]) # ���˵��ַ�����С�ڵ���1��Ԫ��
print([elem for elem in li05 if elem != "b"]) # ���˵�������b��Ԫ��
print([elem for elem in li05 if li05.count(elem) > 1]) # ���˵����ִ���С�ڵ���1�ε�Ԫ��
# coding=gbk
'''list 常用操作'''
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[2])
print(li[0:3]) # 集合切片左闭右开

# list 增加元素
li.append("new")
print(li)

li.insert(2,"02cheng")
print(li)

li02 = [1,2,3]
li.extend(li02)
print(li)

# list 搜索
print(li.index("new"))

# list 删除元素
li.remove("new") # 删除首次出现的一个值
li.pop() # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。


# 使用join链接list成为字符串
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

# list 分割字符串
print(paramsStr.split("&"))

# list 的映射解析
list03 = [1,2,3,4]
print([i*2 for i in list03])

# dictionary 中的解析
dic = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(dic.keys()) # 获取字典中所有键
print(dic.values()) # 获取字典中所有值
print(["%s=%s"%(k,v) for k,v in dic.items()]) # 把字典解析成集合

# list 过滤
li05 = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li05 if len(elem) > 1]) # 过滤掉字符长度小于等于1的元素
print([elem for elem in li05 if elem != "b"]) # 过滤掉不等于b的元素
print([elem for elem in li05 if li05.count(elem) > 1]) # 过滤掉出现次数小于等于1次的元素
#coding=gbk
'''JSON 数据解析'''
import json

# python 字典转json对象，对数据进行编码 dumps()
data = {
    "url": "http://www.baidu.com",
    "no": "123456",
    "name": "joke"
}
dataJson = json.dumps(data)
print("dict格式源数据：", data)
print("json对象：", dataJson)

# python json对象转字典，对数据进行解码 loads()
dataJson = '{"url": "http://www.baidu.com","no": "123456","name": "joke"}'
data = json.loads(dataJson)
print("json对象源数据：", dataJson)
print("dic格式：", data)
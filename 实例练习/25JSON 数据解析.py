#coding=gbk
'''JSON ���ݽ���'''
import json

# python �ֵ�תjson���󣬶����ݽ��б��� dumps()
data = {
    "url": "http://www.baidu.com",
    "no": "123456",
    "name": "joke"
}
dataJson = json.dumps(data)
print("dict��ʽԴ���ݣ�", data)
print("json����", dataJson)

# python json����ת�ֵ䣬�����ݽ��н��� loads()
dataJson = '{"url": "http://www.baidu.com","no": "123456","name": "joke"}'
data = json.loads(dataJson)
print("json����Դ���ݣ�", dataJson)
print("dic��ʽ��", data)
'''生成随机数'''
import random
print(random.random()) # [0, 1).
print(random.randint(0,10)) # 返回范围[a, b]内的随机整数，包括两个端点
print(random.randrange(10,100,10)) # 从范围(start, stop[， step])中随机选择一个项目,step：步长
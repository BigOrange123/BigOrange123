# 定义people类
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性
    __weighet = 0
    # 定义构造函数
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weighet = weight
    # 打印函数
    def stamp(self):
        print("%s说：我的年纪是：%d，我的体重是：%d。"%(self.name, self.age, self.__weighet))

# 实例化people类
pep = people("德玛西亚", 100, 500)
pep.stamp()

# people父类
class parent:
    def myMethod(self):
        print('父类方法')

# sun子类
class sun(parent):
    p = parent()
    # 调用父类方法
    p.myMethod()
    # 重写父类方法
    def myMethod(self):
        print("子类方法")
# 实例化sun类
sun = sun()
# 调用sun类的方法
sun.myMethod()
# from .Pfile import fileTools
# fileTools = fileTools()
# fileTools.fileRead()
# i = 10
# print("hello world")

'''
这是一个多行的
注解
'''

#               Python 条件语句
# 条件语句 if elif else
# if True:
#     print("True")
# else:
#     print("False")
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# print("stirng"+"string")
# print("string"*2)
#
# a = 2
# b = 3
# print函数默认换行输出
# print(a)
# print(b)
# 使print函数不换行输出
# print(a, end=" ")
# print(b)

#               Python 模块导入
# import 与 from...import

# 在 python 用 import 或者 from...import 来导入相应的模块。

# 将整个模块(somemodule)导入，格式为： import somemodule

# 从某个模块中导入某个函数,格式为： from somemodule import somefunction

# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

# 将某个模块中的全部函数导入，格式为： from somemodule import *

#               Python 循环语句
# while 循环
# number = 10
# guess = -1
# while True:
#     try:
#         guess = int(input("请输入数字："))
#         if guess == number:
#             print("恭喜你，猜对了！")
#             break
#         elif guess > number:
#             print("很遗憾，猜大了！")
#         elif guess < number:
#             print("很遗憾，猜小了！")
#     except ValueError:
#         print("你输入的值有问题！")
#
# num = 100
# count = 0
# sum = 0
# while count <= num:
#     sum = sum + count
#     count += 1
# print("1-"+str(num)+"之和等于："+str(sum))

# for 循环 ，break 跳出当前循环
# list01 = [1,2,3,4,5,6]
# for i in list01:
#     if i==3:
#         print("我是："+str(i))
#     if i==5:
#         break # 跳出当前循环
#     print(i)

#for 循环 ，continue 跳出本次循环
# str = "hello word!"
# for i in str:
#     if i == 'o':
#         continue
#     print("我是字母："+i)

# 迭代器有两个基本的方法：iter() 和 next()
# list01 = ["str",5,9,"list"]
# it = iter(list01) # 为list01创建迭代器对象
# for i in it:
#     print(i, end=" ")

#               Python 函数
# def 函数名（参数列表）:
#     函数体
# def hello():
#     print("这是一个hello函数")
# hello() # 函数调用
#
# def area(width,height):
#     return width * height
# result = area(10,5) # 用变量接收有返回值的函数
# print(result)

# def printinfo(name, age):
#     "打印任何姓名和年龄"
#     print("姓名：", name, "年纪：", age)
#     print("姓名："+name, "年纪："+str(age))
#     print("姓名：%s 年纪：%d" %(name, age))
# printinfo("吕布", 18)

# lamdba 匿名函数
# sum = lambda a, b : a + b
# print("值相加后的结果：", sum(10,20))

# return 返回值函数
# def sum(x, y):
#     total = x + y
#     return total
# sum_result = sum(100, 200)
# print("调用sum函数后的值:", sum_result)

# def remove_o():
#     list = ["o", 123, 456, "o"]
#     for i in list:
#         if i == "o":
#             list.remove(i)
#     print(list)
# remove_o()

# 方法	描述
# list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
# list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
# list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
# list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
# list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
# list.clear()	移除列表中的所有项，等于del a[:]。
# list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
# list.count(x)	返回 x 在列表中出现的次数。
# list.sort()	对列表中的元素进行排序。
# list.reverse()	倒排列表中的元素。
# list.copy()	返回列表的浅复制，等于a[:]。

# 列表当作堆栈使用，append()入栈函数，pop()出栈函数，遵循后进先出原则
# list = ["a", 123, 456, "str"]
# list.append("吕布")  # 入栈
# print(list)
# list.pop()  # 出栈
# print(list)
# # 列表当中队列使用
from collections import deque
# queue = deque([1, 2, 3])
# queue.appendleft(321)
# print(queue)
# queue.popleft()
# print(queue)

# from Pfile.fileTools import fileRead
# fileRead()
# from Pfile import fileTools
# fileTools.fileRead()
# result = fileTools.fileabc.abc(1,2,3,4)
# print(result)
from myClass import person
p = person.people("德玛西亚皇子", 100, 500)
p.stamp()


def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

num = 10
def inners():
    global num   # global关键字声明
    num = 100
    print(num)
inners()
print(num)
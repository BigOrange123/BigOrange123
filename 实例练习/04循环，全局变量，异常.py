'''循环，全局变量，异常'''

def quadratic():
    while True:
        try:
            while True:
                global a
                a = float(input("输入数字a："))
                if a != 0:
                    break
            global b,c
            b = float(input("输入数字b："))
            c = float(input("输入数字c："))
        except:
            print("请输入数字")
        else:
            # 异常则不打印，正常则打印
            print("a的值是：{0}".format(a))
            print("b的值是：{0}".format(b))
            print("c的值是：{0}".format(c))
        if a == b == c:
            break
quadratic()

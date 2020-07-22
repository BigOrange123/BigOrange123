'''判断奇数偶数'''
while True:
    try:
        num = int(input("输入一个正整数："))
        if (num % 2) == 0:
            print("{0}是偶数".format(num))
            break
        else:
            print("{0}是奇数".format(num))
            break
    except:
        pass
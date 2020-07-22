'''if 语句'''
def compare():
    while True:
        try:
            num = float(input("输入数字："))
            if num > 0:
                print("{0}：是正数".format(num))
                break
            elif num == 0:
                print("{0}：既不是正数，也不是负数".format(num))
                break
            elif num < 0:
                print("{0}：是负数".format(num))
                break
        except:
            pass

compare()
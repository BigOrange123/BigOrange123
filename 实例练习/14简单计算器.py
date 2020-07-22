'''简单计算器'''

'''方法类class：publicMethods'''
class publicMethods:
    # 加法
    def add(self,x,y):
        return x + y
    # 减法
    def subtraction(self,x,y):
        return x - y
    # 乘法
    def multiplication(self,x,y):
        return x * y
    # 除法
    def division(self,x,y):
        return x / y

'''业务逻辑类class：control'''
class control:
    publicMethods = publicMethods()
    print("选择运输方式：")
    print("\t加法：1")
    print("\t减法：2")
    print("\t乘法：3")
    print("\t除法：4")
    while True:
        try:
            choice = int(input("请输入1/2/3/4："))
            x = float(input("请输入第一个数："))
            y = float(input("请输入第二个数："))
            if choice == 1:
                result = publicMethods.add(x,y)
                print("计算结果：{0}".format(result))
                break
            elif choice == 2:
                result = publicMethods.subtraction(x,y)
                print("计算结果：{0}".format(result))
                break
            elif choice == 3:
                result = publicMethods.multiplication(x,y)
                print("计算结果：{0}".format(result))
                break
            elif choice == 4:
                result = publicMethods.division(x,y)
                print("计算结果：{0}".format(result))
                break
        except:
            print("格式不正确，重新输入")
if __name__ == '__main__':
    control = control()
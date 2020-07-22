# class fileTools():
# 写文件函数
def fileWrite():
    # 打开一个文件，并开启文件流
    f = open("../file/hello.txt", "a+", encoding="GBK")
    # 文件写入内容
    f.write("\n这是一个刚刚写入的文本：\n                    德玛西亚")
    # 关闭文件流
    f.close()

# 读文件函数
def fileRead():
    f = open("../file/hello.txt", "r")
    str = f.read()
    print(str)
    f.close()

# class fileabc():
#     def abc(self,a,b,c):
#         sum = a+b+c
#         return sum

# if __name__ == '__main__':
#     fileRead()
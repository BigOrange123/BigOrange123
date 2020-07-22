'''文件读取'''
from 实例练习工具 import fileTools
fw = fileTools.fileWrite("../file/练习.txt")
fw.write("这是第一行\n")
fw.write("这是第二行\n")
fw.close()

fr,txt = fileTools.fileRead("../file/练习.txt")
print("读取到的文件内容是：\n{0}".format(txt))
fr.close()
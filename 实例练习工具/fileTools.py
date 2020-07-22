'''文件工具'''
# 写文件
def fileWrite(path):
    fw = open(path,"a+",encoding="GBK")
    return fw

# 读文件
def fileRead(path):
    fr = open(path,"r")
    txt = fr.read()
    return fr,txt
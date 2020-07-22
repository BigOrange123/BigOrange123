'''计算三角形面积'''
def area():
    a = float(input("请输入三角形的第一边："))
    b = float(input("请输入三角形的第二边："))
    c = float(input("请输入三角形的第三边："))
    s = (a+b+c)/2 # 计算出三角形的半周长
    area = (s*(s-a)*(s-b)*(s-c))**0.5 # 计算公式
    print("a边长：{0}，b边长：{1}，c边长：{2}；三角形面积：{3}".format(a,b,c,area))
area()
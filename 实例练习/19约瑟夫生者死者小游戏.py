#coding=gbk
'''约瑟夫生者死者小游戏'''
'''
30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
'''

peopleList = []
for p in range(1,31):
    peopleList.append(p)

def game():
    atuo = 0
    count = 0
    for pl in peopleList:
        atuo+=1
        if atuo == 9:
            atuo = 0
            count +=1
            print(pl)
            # game()
            if count == 15:
                break
game()
print(peopleList)
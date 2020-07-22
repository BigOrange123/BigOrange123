'''判断字符串是否为数字
unicodedata.numeric : 将Unicode字符(chr)转换为等效的数值
'''
import unicodedata

def is_numbers(num):
    try:
        num = unicodedata.numeric(num)
        return True,num
    except:
        return False,num

print(is_numbers("4"))
print(is_numbers("四"))
print(is_numbers("你好"))
print(is_numbers("٥")) # 阿拉伯语 5
print(is_numbers("๒")) # 泰语 2
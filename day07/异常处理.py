"""
异常处理
        1.结构
        try:

        except 异常类型 as e:
"""
try:
    open("1.txt","r")
    10/0
    print(num)
except (NameError, IOError) as e:
    print("产生错误")
    print(e)

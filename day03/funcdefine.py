"""函数"""

"""
函数定义
        1.格式 def 函数名(参数1,参数2,...):
                    函数体
        2.调用 函数名()
无参函数
def print_name():
    print("张三")
print_name()

有参函数

a1 = int(input("请输入第一个数:"))
a2 = int(input("请输入第一个数:"))

def sumnum(a, b):
    result = a+b
    print("%d+%d=%d"%(a,b,a+b))
sumnum(a1, a2)

# 函数的多个return
def test():
    a = 11
    b = 22
    c = 33
    # 第一种方式
    # d = [a, b, c]
    # 第二种方式
    # return [a, b, c]
    # 第三种方式
    # return (a, b, c)
    # 第四种方式
    return a, b, c
num = test()
print(num)

# 函数的嵌套

def sum_num(a, b, c):
    result = a+b+c
    return  result
def avg_num(a1, b1, c1):
    result = sum_num(a1, b1, c1)
    result /=3
    return result

avg = avg_num(11, 22, 34)
print(avg)

"""




















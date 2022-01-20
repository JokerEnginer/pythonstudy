"""
闭包概念:在一个外函数中定义了一个内函数,内函数里运用了外函数的临时
        变量,并且外函数的返回值是内函数的引用
"""


def out_fun(number1):
    def in_fun(number2):
        print(number1 + number2)
    return in_fun


f1 = out_fun(100)
f1(100)
f1(200)
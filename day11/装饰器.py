"""
需求: 每个基础部门都有相关的功能, 但后期需要添加验证功能,需要遵循"开放封闭"原则, 既原有功能的代码不能修改
    可以通过装饰器的形式去改

"""
# 部门基础功能
def fun1():
    print("---fun1---")

def fun2():
    print("---fun2---")

def fun3():
    print("---fun3---")

def w1(fun):
    def in_fun():
        print("验证中...")
        fun()
    return in_fun

f1 = w1(fun1)
f1()
f2 = w1(fun2)
f2()

fun3 = w1(fun3)
fun3()
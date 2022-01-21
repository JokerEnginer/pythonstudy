"""
需求: 每个基础部门都有相关的功能, 但后期需要添加验证功能,需要遵循"开放封闭"原则, 既原有功能的代码不能修改
    可以通过装饰器的形式去改

"""

def w1(fun):
    def in_fun():
        print("验证中...")
        fun()
    return in_fun
# 部门基础功能
# python解释器在执行到这行代码的时候就已经开始装饰了,而不需要等到调用函数才开始装饰
@w1
def fun1():
    print("---fun1---")
@w1
def fun2():
    print("---fun2---")
@w1
def fun3():
    print("---fun3---")



# f1 = w1(fun1)
# f1()
# f2 = w1(fun2)
# f2()
# fun3 = w1(fun3)
# fun3()
# 调用函数之前已经装饰成功
fun1()
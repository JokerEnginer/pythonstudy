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
"""
# 全局变量跟局部变量
a = 0   #定义全局变量
def fun1():
    global a #对全局变量进行修改,如果是字典和列表做全局变量,函数内部使用可以不用global修饰
    a = 32
def fun2():
    print("a=%d"%a)
fun1()
fun2()
# 局部变量与全局变量名字相同
如果定义了局部变量,优先使用局部变量,如果没有定义局部变量,会使用全局变量

a = 10
def fun1():
    a = 20
    print(a)
def fun2():
    print(a)
fun1()
fun2()
"""
"""
缺省参数
        1.定义函数给形参传递初始值
        2.函数调用需要给指定参数传值,不传使用形参初始值.如果调用函数传值
        变量名需要跟形参一致

def fun1(a, b, c=33):
    print(a)
    print(b)
    print(c)
fun1(11, 22)
fun1(11, 22, c=44)
# fun1(a=1, b=2,A=44) 报错了,命名参数与形参不一致

# 不定长参数

def num1(a, b,c=3, *args ):
    sumnum = 0
    for i in args:
        sumnum += i
    result = sumnum+a+b
    print(result)
num1(1,2,3,4,5,6,c=7)

*args:传进的所有参数都会被args变量收集，
它会根据传进参数的位置合并为一个元组(tuple)，
args是元组类型，这就是包裹位置传递。
** kwargs:kargs是一个字典(dict)，收集所有关键字参数

def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
A = (11,33,55)
B = {"name":"lisi","age":18}
test(1,2,3,4,5,6,t=7,y=9)
test(77, 99, A, B)
test(77, 99, *A, **B)   #拆包把字典或者元组拆开包装


# 引用
a = 100
b = a
print(id(a))
print(id(b))
"""






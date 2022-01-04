# 父类中的私有属性与私有变量子类无法继承,但是可以通过父类定义非私有方法调用私有方法
# 子类在调用父类中的方法

class A():
    def __init__(self):
        self.num = 100
        self.__num1 = 200
    def test(self):
        print("----hhhh----")

    def __test(self):
        print("---私有方法---")

    def text1(self):
        self.__test()


class B(A):
    pass

b = B()
print(b.num)
# print(b.__num)
b.test()
# b.__test()
b.text1()
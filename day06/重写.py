# 调用被重写的父类的方法
class Animal():
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")
    def run(self):
        print("-----跑-----")
    def sleep(self):
        print("-----睡-----")


class Dog(Animal):
    def bar(self):
        print("----汪汪叫----")


class WangCai(Dog):

    def bar(self):
        print("---撕心裂肺的叫---")

        # 第一种调用被重写的父类的方法
        #Dog.bar(self)
        #第二种调用被重写的父类的方法
        super().bar()

wangcai = WangCai()
wangcai.bar()


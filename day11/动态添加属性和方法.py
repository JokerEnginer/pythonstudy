import types

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 给对象添加方法
def eat(self):
    print("正在吃...")


# 添加类方法
@classmethod
def run(cls):
    print("runing...")
@staticmethod
def sing():
    print("sing...")

p1 = Person("laowang", 15)
print(p1.name, p1.age)
p1.eat = types.MethodType(eat, p1)  #给对象添加方法,通过types.MetthodType(方法名,对象)添加
p1.eat()
Person.run = run
Person.sing = sing
Person.run()
Person.sing()
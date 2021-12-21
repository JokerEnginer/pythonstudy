
# 定义类
class Cat():
    def eat(self):
        print("猫正在吃鱼")
    def drink(self):
        print("猫正在喝酒")
    def introduct(self):
        print("%s\t%d"%(self.name, self.age))

# 创建对象
tom = Cat()
# 调用类方法
tom.eat()
tom.drink()
#添加类属性
tom.name = "Tom"
tom.age = 2
print(tom.name)
tom.introduct()
#创建新的对象
loy = Cat()
loy.name = "loy"
loy.age = 20
loy.introduct()
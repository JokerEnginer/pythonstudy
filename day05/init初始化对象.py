class Cat():
    # 初始化对象
    #创建对象的时候,会自动调用init方法
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
        print("初始化了....")

    def eat(self):
        print("正在吃鱼")

    def drink(self):
        print("猫正在喝酒")
    def introduce(self):
        print("%s\t%d"%(self.name, self.age))

tom = Cat("tom", 30)
tom.introduce()

miaomiao = Cat("蓝猫",20)
tom.introduce()




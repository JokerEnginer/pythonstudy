class Animal():
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")
    def run(self):
        print("-----跑-----")
    def sleep(self):
        print("-----睡-----")


class Cat(Animal):
    def bar(self):
        print("---吼叫---")

tom = Cat()
tom.eat()
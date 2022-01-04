"""
不同的子类调用相同的父类方法，产生不同的执行结果，可以增加代码的外部灵活度。
多态是以继承和重写父类方法为前提的，它是一种调用方法的技巧，不会影响到类的内部设计。
"""
class Dog():
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print("---追击犯人---")


class DrugDog(Dog):
    def work(self):
        print("---追击毒贩---")

class Person():
    def work_with_dog(self, dog):
        dog.work()

ad = ArmyDog()
dd = DrugDog()
p = Person()
p.work_with_dog(ad)
p.work_with_dog(dd)
# 在多继承中,如果子类与父类有重名的方法,现在子类中寻找,然后驱动父类中寻找
# 可以通过类名.__mro__去查询 顺序
class Base(object):
    def test(self):
        print("---base---")

class A(Base):
    def test(self):
        print("---A---")

class B(Base):
    def test(self):
        print("---B---")

class C(A, B):

    print("---C---")


c = C()
c.test()
print(C.__mro__)
class Person(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

p = Person()
print(p.money)
p.money = 100
print(p.money)
class Dog():
    def __init__(self, age, name):
        #通过下划线对属性进行修饰
        self.__age = age
        self.__name = name

    def setage(self, age):
        if self.__age >0 and self.__age<100:
            self.__age = age
        else:
            self.__age = 0
    def getage(self):
        return  self.__age
dog = Dog(19,"憨憨")
# dog.age = 20
# dog.setage(-10)
age = dog.getage()
print(age)
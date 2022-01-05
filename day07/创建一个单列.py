class Dog(object):
    __instance = None
    __first_init = False
    def __new__(cls, *args, **kwargs):

        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self,name, age):
        if not self.__first_init:
            self.name = name
            self.age =age
            Dog.__first_init=True

d1 = Dog("tom", 19)

d2 = Dog("cc", 20)
print(id(d1))
print(id(d2))

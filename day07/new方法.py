class A(object):

    def __init__(self):
        print("这是init方法")

    def __del__(self):
        print("这是del 方法")

    def __new__(cls, *args, **kwargs):
        print(id(cls))
        print("这是new方法")
        return object.__new__(cls)

print(id(A))

a = A()
#相当于new负责创建,init负责初始化
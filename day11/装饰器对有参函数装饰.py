# 装饰器对有参函数进行装饰时,只要对内部函数记性传参数就可以了,
# 外部函数需要传入函数的引用


def out_wraper1(func):
    print("---装饰1---")
    def in_wraper1(a, b):
        func(a, b)
    print("---装饰2---")
    return in_wraper1


def out_wraper2(func):
    print("---装饰1---")
    def in_wraper2(*args, **kwargs):
        func(*args, **kwargs)
    print("---装饰2---")
    return in_wraper2


@out_wraper1
def test1(a, b):
    print("%d %d"%(a, b))
test1(1, 2)

@out_wraper2
def test1(a, b,c,d):
    print("%d %d %d %d"%(a, b, c, d))
test1(1, 2, 3, 4)

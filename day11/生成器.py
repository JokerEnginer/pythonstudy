#列表生成式
a = [i for i in range(10)]
print(a)
# 生成器的第一种方式,把列表生成式中的[]改为()
b = (i for i in range(10))
print(b)
print(next(b))

# 生成器的第二种方式,通过yield的形式创建生成器,yield会返回一个值

def fib():
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a+b

c = fib()
print(type(c))
print(next(c))

# 使用for循环遍历迭代器
for i in c:
    print(i)

# c.__next__()与next(c)是等价的
# print(c.__next__())  如果生成器没有值,就会报错StopIteration
# next(c)
# 可迭代对象 Iterable: list dict set str tuple
#迭代器对象 Iterator,可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
'''
凡是可作用于for 循环的对象都是 Iterable 类型；
凡是可作用于next() 函数的对象都是 Iterator 类型
集合数据类如 list 、 dict 、 str 等是 Iterable 但不是 Iterator ，不过可以通过 iter() 函数获得一个 Iterator 对象。
'''
from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))  # 可迭代对象
print(isinstance([], Iterator)) # 迭代器
print(isinstance((i for i in range(10)), Iterator))

print("*"*50)
# 使用iter()将可迭代对象转成迭代器,
a = [1, 2, 3, 4]
print(isinstance(a, Iterator))
print(isinstance(iter(a), Iterator))

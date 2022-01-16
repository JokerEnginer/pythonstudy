"""
is :比较两个引用是否相等,及两个引用是否指向了同一个对象
==:比较两个对象是否相等
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a == c)
print(b == c)
print(a is b)
print(a is c)
print(b is c)
print("-------------------")
# x = 100
# y = 100
x = 100000
y = 100000
print(x is y)
print(x == y)

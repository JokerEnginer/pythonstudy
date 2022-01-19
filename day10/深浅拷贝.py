# 浅拷贝:拷贝了引用,没有拷贝内容
# 深拷贝:对对象的所有拷贝,递归
#深浅拷贝元组和列表有区别,可以通过copy()来区分数据类型是否可变

from copy import deepcopy
from copy import copy
# 浅拷贝
a = [1, 2, 3, 4]
b = a
a.append(5)
print(a)
print(b)

# 深拷贝
c = [11, 22, 33, 44, 55]
d = deepcopy(c)
c.append(66)
print(c)
print(d)
#copy() 可以区分数据是否可修改
print("-------------------------------")
f = [1, 2, 3]
g = [4, 5, 6]
h = [f, g]
i = copy(h)
f.append(66)
print(h[0], id(h))
print(i[0], id(i))
print("----------------------------------")
f = [1, 2, 3]
g = [4, 5, 6]
h = (f, g)   # 不可变类型,直接同一个引用
i = copy(h)
f.append(66)
print(h[0], id(h))
print(i[0], id(i))


# deepcopy()
print("-------------------------------")
l = [1, 2, 3]
m = [4, 5, 6]
n = [l, m]
o = deepcopy(n)
l.append(66)
print(n[0], id(n))
print(o[0], id(o))
# 浅拷贝:拷贝了引用,没有拷贝内容
# 深拷贝:对对象的所有拷贝,递归
from copy import deepcopy
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
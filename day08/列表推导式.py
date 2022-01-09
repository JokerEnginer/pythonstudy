
a = [i for i in range(1, 20, 2)]
print(a)

b = [i for i in range(1,20) if i%2==0]
print(b)

c = [i for i in range(3) for j in range(2)]
print(c)

d = [(i, j) for i in range(3) for j in range(2)]
print(d)


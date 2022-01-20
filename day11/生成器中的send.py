def test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

c = test()
print(c.__next__())
print(c.send("python"))
print(c.__next__())
print(c.send("python"))
print(c.__next__())
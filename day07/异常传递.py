def test1():
    print("--test1-1---")
    print(num)
    print("--test1-2---")

def test2():
    print("---test2-1---")
    test1()
    print("---test2-2---")


def test3():
    try:
        print("---test3-1---")
        test1()
    except NameError as e:
        print("错误信息是:%s"%(e))
    print("--test3-2---")

test3()



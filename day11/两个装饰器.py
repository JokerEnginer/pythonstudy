

def makeBold(fun):
    def wraper_in():
        print("---1---")
        return '<b>'+fun()+'</b>'
    return wraper_in


def makeItalics(fun):
    def wraper_in():
        print("---2---")
        return '<i>'+fun()+'</i>'
    return wraper_in


@makeBold
def test1():
    return "Hello World-1"

@makeItalics
def test2():
    return "Hello World-2"

@makeBold
@makeItalics
def test3():
    print("---3---")
    return "Hello World-3"

t1 = test1()
print(t1)

t2 = test2()
print(t2)

t3 = test3()
print(t3)


def out_wraper(func):
    def in_wraper():
        return func() # 对于有返回值的函数,如果此处不返回函数,那么13行就会返回一个None
    return in_wraper

@out_wraper
def test():
    print("---test---")
    return "hello world"

ret = test()
print(ret)
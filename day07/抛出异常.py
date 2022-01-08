# 自定义异常类
# 需要继承Exception类
class SortInputException(Exception):
    def __init__(self,length, atleastlen):
        self.length = length
        self.atleastlen = atleastlen


def test():

    try:
        con = input("请输入内容")
        if len(con) < 3:
            raise SortInputException(len(con), 3)


    except SortInputException as e:
        print("SortInput:输入长度是%d,长度至少是%d"%(e.length, e.atleastlen))

    else:
        print("没有异常")

test()
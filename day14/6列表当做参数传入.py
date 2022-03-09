# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 6列表当做参数传入.py
# @Software: PyCharm

from threading import Thread
import time

g_num = [11,22,33,44]


def worker1(nums):
    nums.append(55)
    print("in worker1 ", nums)


def worker2(nums):
    time.sleep(1)
    print("in worker2  ", nums)


t1 = Thread(target=worker1, args=(g_num, ))
t1.start()

t2 = Thread(target=worker2, args=(g_num, ))
t2.start()
# 总结: 当列表作为参数传递到线程中,数据也是共享的,与全局变量是一样的效果
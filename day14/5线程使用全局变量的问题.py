# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 5线程使用全局变量的问题.py
# @Software: PyCharm

from threading import Thread
import time

g_num = 0


def fun1():
    for i in range(1000000):
        global g_num
        g_num += 1
    print("fun1 g_num is %d" % g_num)


def fun2():
    for i in range(1000000):
        global g_num
        g_num += 1
    print("fun2 g_num is %d" % g_num)


t1 = Thread(target=fun1)
t1.start()

time.sleep(3)
t2 = Thread(target=fun2)
t2.start()
time.sleep(3)
print(" g_num is %d" % g_num)

'''
总结:1,在一个进程内的所有线程共享全局变量，能够在不适用其他方式的前提下完成多线程之间的数据共享
    2,缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）
'''

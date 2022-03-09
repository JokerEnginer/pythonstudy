# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 7解决一百万次的bug.py
# @Software: PyCharm

from threading import Thread
import time

g_num = 0
g_flag = 1

def worker1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1
        g_flag = 0

        print("--in worker1 ",g_num)


def worker2():
    global g_num
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break
    print("in worker2 ",g_num)



t1 = Thread(target=worker1)
t1.start()

t2 = Thread(target=worker2)
t2.start()


# 总结:使用g_flag变量控制执行的顺序,会浪费cpu很多资源,不建议使用
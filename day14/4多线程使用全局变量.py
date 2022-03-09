# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 4多线程使用全局变量.py
# @Software: PyCharm

from threading import Thread
import time

g_num = 1000

def fun1():
    global g_num
    for i in range(3):
        g_num +=1
    print("fun1 g_num is %d"%g_num)

def fun2():
    global g_num
    print("fun2 g_num is %d" % g_num)

print("线程启动之前g_num is %d" % g_num)

t1 = Thread(target=fun1)
t1.start()
time.sleep(1)
t2 = Thread(target=fun2)
t2.start()
# 总结:线程的全局变量是共用的,进程的全局变量是独立的
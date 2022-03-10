# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 8使用互斥锁.py
# @Software: PyCharm

from threading import Lock, Thread
import time

g_num = 0

def worker1():
    global g_num
    # 这个线程和worker2线程都抢着对这锁进行上锁,如果一方成功的上锁,你们导致另外一方会堵塞(一直等待)
    # 直到之歌锁被解开为止
    lock.acquire()
    for i in  range(1000000):
        g_num += 1
    lock.release()   # 用来对lock指向的这个锁进行解锁,只要开了锁,那么加下来会让所有因为这个锁被上了锁 而
    # 堵塞的进程,进行抢着上锁
    print("in worker1 ",g_num)


def worker2():
    global g_num
    lock.acquire()
    for i in  range(1000000):
        g_num += 1
    lock.release()
    print("in worker2 ",g_num)
# 创建一把互斥锁
lock = Lock()
t1 = Thread(target=worker1)
t1.start()
t2 = Thread(target=worker2)
t2.start()



# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 9多线程使用非共享变量.py
# @Software: PyCharm

from threading import Thread
import time
import threading

def worker():
    name = threading.current_thread().name
    print("threading name is %s"%name)
    num = 100
    if name =="Thread-1":
        num += 1
    else:
        time.sleep(2)
    print("theading name is %s----%d"%(name,num))

t1 = Thread(target=worker)
t1.start()

t2 = Thread(target=worker)
t2.start()


# 总结:线程使用非共享变量时,不需要加锁
# 在多线程开发中，全局变量是多个线程都共享的数据，而局部变量等是各自线程的，是非共享的
# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 10应用同步.py
# @Software: PyCharm

from threading import Thread, Lock
import time


class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("task1")
                time.sleep(0.5)
                lock2.release()


class Tast2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("task2")
                time.sleep(0.5)
                lock3.release()


class Tast3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("task3")
                time.sleep(0.5)
                lock1.release()


lock1 = Lock()
lock2 = Lock()
lock2.acquire()
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Tast2()
t3 = Tast3()
t1.start()
t2.start()
t3.start()
# 总结：可以使用互斥锁完成多个任务，有序的进程工作，这就是线程的同步

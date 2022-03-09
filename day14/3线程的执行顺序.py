# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 3线程的执行顺序.py
# @Software: PyCharm

from threading import Thread
import time


class MyThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "i am"+self.name + "==="+str(i)
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()

# 总结线程的执行顺序是无序的
# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 6join子进程.py
# @Software: PyCharm



from multiprocessing import Process
import time
import random


def test():
    for i in range(random.randint(1,5)):
        print("-----%d------"%i)
if __name__ == '__main__':

    p = Process(target=test)
    p.start()
    p.join()  # join([timeout])：是否等待进程实例执行结束，或等待多少秒；
    print("main")

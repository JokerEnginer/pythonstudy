# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 4Process类创建进程.py
# @Software: PyCharm


from multiprocessing import Process
import time


def test():
    while True:
        print("test..")
        time.sleep(1)



if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    while True:
        print("main")
        time.sleep(1)

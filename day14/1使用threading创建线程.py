# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 1使用threading创建线程.py
# @Software: PyCharm

from threading import Thread
import time
def test():
    print("晚上吃太多了,一直在放屁")
    time.sleep(1)


for i in range(5):
    t = Thread(target=test)
    t.start()

# 如果多个线程执行的都是同一个函数的话,线程之间不会有影响
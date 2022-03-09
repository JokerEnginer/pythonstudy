# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 2使用Thread子类创建线程.py
# @Software: PyCharm


from threading import Thread
import time
class MyThread(Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "i am "+self.name+"--"+str(i)
            print(msg)


mythread = MyThread()
mythread.start()


# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 7process子类创建子进程.py
# @Software: PyCharm



from multiprocessing import Process
import time

class MyProcess(Process):
    # run()：如果没有给定target参数，对这个对象调用start()方法时，就将执行对象中的run()方法；
    def run(self):
        while True:
            print("---1----")
            time.sleep(1)

if __name__ == '__main__':

    p = MyProcess()
    p.start()

    while True:
        print("main")
        time.sleep(1)


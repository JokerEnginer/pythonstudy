# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 5给target函数传递参数.py
# @Software: PyCharm


from multiprocessing import Process
import time
import os

def p_fun(name):
    print("子进程进行中,name=%s,pid=%d"%(name, os.getpid()))




if __name__ == '__main__':
    print('父进程 %d.' % os.getpid())
    p = Process(target=p_fun, args=("test",))
    print('子进程将要执行')
    p.start()
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('子进程已结束')


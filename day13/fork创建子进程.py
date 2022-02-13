# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: fork创建子进程.py
# @Software: PyCharm

import os
import time
ret = os.fork() # 在windows不能使用

# 程序执行到os.fork()时，操作系统会创建一个新的进程（子进程），然后复制父进程的所有信息到
# 子进程中
# 然后父进程和子进程都会从fork()函数中得到一个返回值，在子进程中这个值一定是0，而父进程中
# 是子进程的 id号
if ret == 0:
    while True:
        print("----------1------------id%d"%os.getpgid())
        time.sleep(1)

else:
    while True:
        print("----------2------------id%d"%os.getppid())
        time.sleep(1)


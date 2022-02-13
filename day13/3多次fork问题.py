# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 3多次fork问题.py
# @Software: PyCharm


import time
import os


ret = os.fork()
if ret == 0:
    print("-------1-------")

else:
    print()

# 总结:父进程、子进程执行顺序没有规律，完全取决于操作系统的调度算法


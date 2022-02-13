# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 2多进程修改全局变量.py
# @Software: PyCharm

import os
import time

num = 100
ret = os.fork()
if ret == 0:
    print("----子进程-----")
    num += 1
    time.sleep(1)
else:
    print("-----父进程-----")
    num += 1
    time.sleep(1)


# 总结:在多进程中,每个进程中所有数据(包括全局变量)都各拥有一份,互不影响

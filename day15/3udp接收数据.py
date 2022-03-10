# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 3udp接收数据.py
# @Software: PyCharm

from socket import *

udpsocke = socket(AF_INET, SOCK_DGRAM)
udpsocke.bind(("",7788))

udpsocke.recvfrom(1024) # 表示本次最大的接收字节数
udpsocke.close()

'''
总结:
一个udp网络程序，可以不绑定，此时操作系统会随机进行分配一个端口，如
果重新运行次程序端口可能会发生变化
一个udp网络程序，也可以绑定信息（ip地址，端口号），如果绑定成功，那么
操作系统用这个端口号来进行区别收到的网络数据是否是此进程的
'''
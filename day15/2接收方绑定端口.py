# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 2接收方绑定端口.py
# @Software: PyCharm

from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)
# 接收方一般绑定,发送方 一般不用
bindadd = ("", 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpsocket.bind(bindadd)
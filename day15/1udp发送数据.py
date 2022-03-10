# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 1udp发送数据.py
# @Software: PyCharm

from socket import *

socketer = socket(AF_INET, SOCK_DGRAM)
# socket每次发送数据,都要有接收方的ip与端口
sender = ("192.168.2.105", 8080)
senddata = b"hhhhh"
socketer.sendto(senddata, sender)
socketer.close()
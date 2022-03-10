# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 4简单聊天室.py
# @Software: PyCharm


from socket import *

# 接收信息方
def main():
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(("", 8866))
    while True:
        recInfo = udpsocket.recvfrom(1024)
        print("[%s]:%s"%(str(recInfo[1]), recInfo[0].decode("utf-8")))


if __name__ == '__main__':
    main()

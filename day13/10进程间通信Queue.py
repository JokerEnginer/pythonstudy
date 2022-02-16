from multiprocessing import Queue,Process

import time
import random

def Qwrite(q):
    for i in ["A", "B","C", "D"]:
        print("put %s in to queue"%i)
        q.put(i) # 将消息写入队列
        time.sleep(1)


def Qreader(q):
    while True:
        if not q.empty(): # 判断队列是否为空
            value = q.get(True) # 获取队列的数据
            print("get %s from queue"%value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':

    q = Queue() # 若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；
    qw = Process(target=Qwrite,args=(q,))
    qr = Process(target=Qreader,args=(q,))
    qw.start()
    qw.join()

    qr.start()
    qr.join()
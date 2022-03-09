# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 11生产者与消费者解耦问题.py
# @Software: PyCharm


from threading import Thread
from queue import Queue
import time


class Producer(Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize()<1000:

                for i in range(100):
                    count += 1
                    msg = "生成品"+str(i)
                    q.put(msg)
                    print(msg)
                time.sleep(1)


class Consumer(Thread):
    def run(self):
        while True:
            if q.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" + q.get()
                    print(msg)
                time.sleep(1)

if __name__ == '__main__':

    q = Queue()
    for i in range(500):
        q.put("初始化产品:"+str(i))
    for i in range(2):
        pro = Producer()
        pro.start()
    for i in range(5):
        con = Consumer()
        con.start()



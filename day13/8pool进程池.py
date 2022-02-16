from multiprocessing import Pool
import os
import time
def worker(num):

    print("----pid = %d---num = %d" % (os.getpid(), num))
    time.sleep(1)
if __name__ == '__main__':
    # 3表示进程池中进程的最大数
    pools = Pool(3)
    for i in range(10):
        print("======%d======"%i)
        pools.apply_async(worker, (i,))
        # 使用非阻塞方式调用func（并行执行，
        # 堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传
        # 递给func的参数列表，kwds为传递给func的关键字参数列表；

    pools.close() # 关闭进程池,不在接受新任务
    pools.join() # 主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；

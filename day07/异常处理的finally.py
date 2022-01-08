import time
try:
    f = open("1.txt")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except IOError:
        pass
    finally:
        # 模拟中途关闭文件,不管过程怎么样,最后都会关闭文件
        f.close()
        print("文件关闭")

except:
    print("没有这个文件")
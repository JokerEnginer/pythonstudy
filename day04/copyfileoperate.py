# 文件复制
"""
思路
    1.打开copyfileold文件
    2.读取内容
    3.写入到copyfilenew文件中
    4.关闭所有文件
"""
fr = open("E:\pyStudyPros\pythonstudy\copyfileold.txt", "r", encoding="utf-8")
fw = open("E:\pyStudyPros\pythonstudy\copyfilenew.txt", "w", encoding="utf-8")
while True:

    content = fr.read(1024)
    if len(content) == 0:
        break
    fw.write(content)
fr.close()
fw.close()
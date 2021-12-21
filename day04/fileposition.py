
"""
tell() 返回文件指针位置
eek(offset, from) 文件定位读取,有两个参数第一个偏移量,
from:方向
0:表示文件开头
1:表示当前位置
2:表示文件末尾

"""


fr = open("E:\pyStudyPros\pythonstudy\copyfileold.txt", "r", encoding="utf-8")
# position = fr.tell()
# print(position)
fr.seek(2, 0)
content = fr.read()
print(content)
fr.close()
# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 2正则数量表达.py
# @Software: PyCharm

import re

print(re.match("\d*", "808080137"))   # 匹配前一个字符出现0次或者无限次
print(re.match("\d+", "89889"))       # 匹配一个字符至少出现一次
print(re.match("\d?", "099"))          #匹配字符出现一次或者0次,要么一次.要么没有
print(re.match("\d?[a-z]", "222dsfas"))
print(re.match("\d{9}", "1234567890aa"))  # {m} 匹配前一个字符出现m次
print(re.match("\d{5,}","12355dfga"))     # {m,} 匹配前一个字符至少出现m次
print(re.match("\d{3,5}", "623348adgaehg")) # {m,n} 匹配前一个字符出现m到n次


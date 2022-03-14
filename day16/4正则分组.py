# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 4正则分组.py
# @Software: PyCharm


import re

s = "<html><h1>我喜欢学习</h1></html>"
print(re.match(r"<.+><.+>.+</.+></.+>", s))    # (ab) 用于括号中的字符作为一个组
print(re.match(r"<(.+)><(.+)>.+</\2></\1>", s)) # \num如\2 引用分组匹配字符串
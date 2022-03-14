# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 1match初使用.py
# @Software: PyCharm


import re

pattern = "hello"  # 规则
s = "hello world"
result = re.match(pattern, s)
print(result.group())

print(re.match(".", "jj").group())  # .匹配任意一个字符
print(re.match("\d\d", "12356"))  # \d 匹配一个数字
print(re.match("\D", "1213"))     # |D 匹配一个非数字
print(re.match("\D", "asdf"))
print(re.match("\s","  "))        # \s匹配空白字符,包括空格 tab键
print(re.match("\S",'sss'))          # 匹配非空白
print(re.match("\w", "hhhshfh"))   # 匹配单词字符
print(re.match("\W", "*#*&"))      # 匹配非单词
print(re.match("1[^2]","18378330625"))  #[] 匹配[]中列举的字符^取反
print(re.match("[a-z]", 'afjakhgais4'))

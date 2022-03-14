# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 5贪婪模式.py
# @Software: PyCharm


import re

# Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；
# 贪婪则相反，总是尝试匹配尽可能少的字符。
# 在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。



s = "This is a number 234-235-22-423"

print(re.match(r"(.+)(\d+-\d+-\d+-\d+)", s).group(1))    # -->This is a number 23
print(re.match(r"(.+?)(\d+-\d+-\d+-\d+)", s).group(1))    # -->This is a number

s1 = """https://anchorpost.msstatic.com/cdnimage/anchorpost/1009/e4/837d557cdf07c6adf85a62540ce53d_0_1627558724.jpg?imageview/0/w/338/h/190/blur/1/format/webp"""

print(re.search(r"https.+", s1).group())
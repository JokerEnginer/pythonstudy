# -- coding: utf-8 --
# @Author  : JokerEngineer
# @FileName: 3正则边界问题.py
# @Software: PyCharm

import re
print(re.match(r"^1[356478]\d{9}", "18378330625"))  # ^匹配字符串开头
print(re.match(r"^1[345678]\d{9}$", "18378330625")) # $匹配字符串结尾
print(re.match(r"^1[345678]\d{9}$", "183783306253"))
print(re.match(r".+ll\b", "hell o"))  # \b匹配一个字符的边界
print(re.match(r".+ll\b", "hello"))
print(re.match(r".+ll\B", "hello"))  # \B匹配非单词边界
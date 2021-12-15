# name = input("请输入名字：")
# print("===================")
# print("这个人的名字是：%s"%name)
# print("===================")
# import keyword
# a = keyword.kwlist
# print(a)
# print(len(a))
# age = int(input("请输入年龄："))
# if age >= 18:
#     print("你可以上网了")
# else:
#     print("回家学习吧")
# a = 10
# b = 3
# print(a//b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(a**b)
# print()
"""
== == == == == == == == == == == == == == == == ==
=        欢迎进入到身份认证系统V1.0
= 1.登录
= 2.退出
= 3.认证
= 4.修改密码
== == == == == == == == == == == == == == == == ==
"""
# print("="*20)
# print("=        欢迎进入到身份认证系统V1.0")
# print("= 1.登录")
# print("= 2.退出")
# print("= 3.认证")
# print("= 4.修改密码")
# print("="*20)
"""
if...elif...elif
num = int(input("请输入1-7:"))
if num ==1:
    print("今天是星期一")
elif num ==2:
    print("今天是星期二")
elif num == 3:
    print("今天是星期三")
elif num == 4:
    print("今天是星期四")
elif num == 5:
    print("今天是星期五")
elif num == 6:
    print("今天是星期六")
elif num ==7:
    print("今天是星期天")
else:
    print("输入有误")
"""
"""
求1-100的和
i = 1
sum = 0
while i<100:
    sum += i
    i +=1
print(sum)

i = 0
sum = 0
while i<100:
    if i%2 == 0:
        sum+=i
    i+=1
print(sum)
"""
i=0
while i<5:
    j= 1
    while j<5:
        print("*",end=' ')
        j+=1
    i+=1
    print()

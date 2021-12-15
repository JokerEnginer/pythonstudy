
"""
length = int(input("到的长度："))
if length > 10:
    print("这个是管制刀具")
else:
    print("可以带上车")
"""

"""
字符串
name = "abcdefAB CbcbcbDEF"
print(name[0])
print(name[2:5])
print(name[2:-2])
print(name[::-1])
print(name.find("bc"))  #找到返回位置索引，没有查到，返回-1
print(name.rfind("bc"))  #查找元素最后一次出现的位置索引
print(name.index("bc")) #找到返回位置索引，没有找到报错
print(name.replace("bc","fuck",1))  #替换字符串中的字符
print(name.split())  #切割字符串，成为新的列表
print(name.capitalize())  #字符串开头大写
print(name.title())   #字符串的每个字符的首字母大写
print(name.startswith("a"))  #以什么开始，返回True和False
print(name.endswith("c"))    #以什么结束，返回True和False
print(name.upper())         #所有字符大写
print(name.lower())         #所有字符小写
print(name.rjust(50))       #右对齐
print(name.ljust(50))       #左对齐
print(name.center(50))      #居中显示
text = name.center(60)
print(text.strip())         #删除 string 字符串的空格.
print(text.rstrip())        #删除 string 字符串末尾的空格.
print(text.lstrip())        #删除 string 字符串左边的空格.
"""
"""
列表
添加：1.append()后面追加
      2.insert()通过索引添加
      3.extend()多个添加
删除：1.pop()  默认删除最后一个，通过正负所以删除
      2.remove()  通过元素删除
      3.del   通过索引删除
修改：列表名[] = 新元素
切片：列表名[::]

names = ["张三", "赵四", "王五"]
names.insert(0,"八戒")
print(names)
names.append("悟空")
print(names)
names2 = ["路飞", "张谋"]
names.extend(names2)
print(names)

names.pop()
print(names)
names.remove("张三")
print(names)
del names[0]
print(names)

# 宿舍管理系统
print("="*50)
print("         名字管理系统")
print("1.添加名字")
print("2.查询名字")
print("3.修改名字")
print("4.删除名字")
print("5.退出程序")
print("="*50)

names = []
while True:
    num = int(input("请输入一个操作数字："))
    if num == 1:
        new_name = input("请输入一个名字：")
        names.append(new_name)
        print(names)
    elif num ==2:
        find_name = input("请输入要查询的名字：")
        if find_name in names:
            print("找到了")
        else:
            print("查无此人")
    elif num ==3:
        change_name = input("请输入一个需要修改的名字：")
        if change_name in names:
            chang_check = input("请输入需要改成啥名字：")
            index_num = names.index(change_name)
            names[index_num]=chang_check
        else:
            print("系统没有这个人")

    elif num == 4:
        del_name = input("请输入一个需要删除的名字：")
        if del_name in names:
            names.remove(del_name)
        else:
            print("系统没有这个人")
    elif num ==5:
        break
    else:
        print("输入错误")
"""

"""
字典
创建
    形式：字典名= {key:vlaue} 键值对
增加
    字典名[key] = 元素  key没有则创建新键值对，如果有则为修改
删除
    del 字典名[key]
修改
    字典名[key] = 元素  key没有则创建新键值对，如果有则为修改
查询
    字典名.get(key)

info = {"name":"张谋", "age":19, "sex":"男"}
info["height"] = 180
print(info)
info["age"] = 22
print(info)
del info["age"]
print(info)
print(info.get("sex"))


#名片管理系统
print("="*50)
print("1.添加名字")
print("2.查询名字")
print("3.修改名字")
print("4.删除名字")
print("5.查询所有")
print("6.退出程序")
print("="*50)
card = []
while True:
    num = int(input("请输入相关的操作"))
    if num ==1:
        new_name = input("请输入名字: ")
        new_qq= input("请输入qq: ")
        new_wechat = input("请输入微信: ")
        new_phone = input("请输入手机号: ")
        new_info = {}
        new_info["name"] = new_name
        new_info["QQ"] = new_qq
        new_info["wechat"] = new_wechat
        new_info["phone"] = new_phone
        #讲字典中的数据插入列表中
        card.append(new_info)
        print(card)

    elif num == 2:
        find_name = input("请输入需要查询的名字：")
        find_flag = 0
        for names in card:
            if find_name == names["name"]:
                print("%s\t%s\t%s\t%s" %(names["name"], names["QQ"], names["wechat"], names["phone"]))
                find_flag = 1
                break
            if find_flag ==0:
                print("查无此人。。。。。。")
    elif num == 3:
        pass
    elif num == 4:
        pass
    elif num == 5:
        print("名字\tQQ\t微信\t手机号")
        for names in card:
            print("%s\t%s\t%s\t%s" %(names["name"], names["QQ"], names["wechat"], names["phone"]))
    elif num == 6:
        break
    else:
        print("请根据系统提示进行操作")
 字典遍历
info = {"name": "张三", "age": 19}
for i in info.keys():
    print(i)
    print(type(i))
for i in info.values():
    print(i)
    print(type(i))
for i, j in info.items():
    print("%s\t%s" % (i, j))
"""

"""
元组
    1.创建:t = (1,2,3,"5")

"""
t = (1,2,3,"5")
print(t)
print(t.count(1))
print(t.index(1))




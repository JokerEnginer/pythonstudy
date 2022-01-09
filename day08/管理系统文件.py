#名片管理系统
print("="*50)
print("1.添加名字")
print("2.查询名字")
print("3.修改名字")
print("4.删除名字")
print("5.查询所有")
print("6.保存信息")
print("7.退出程序")
print("="*50)
card = []
def save_file():
    f = open("F:\pythonstudy\day08\A.data", "w")
    f.write(str(card))

    f.close()





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
        save_file()
    elif num == 7:
        break
    else:
        print("请根据系统提示进行操作")
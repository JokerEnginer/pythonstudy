# 定义一个烤番薯类
"""
1. 分析“烤地瓜”的属性和方法
示例属性如下:
cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，
超过8表示已经烤成木炭了！我们的地瓜开始时时生的
cookedString : 这是字符串；描述地瓜的生熟程度
condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
示例方法如下:
cook() : 把地瓜烤一段时间
addCondiments() : 给地瓜添加配料
__init__() : 设置默认的属性
__str__() : 让print的结果看起来更好一些
"""
class SweetPotato():
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []
    def cook(self,time):
        self.cookedLevel += time
        if self.cookedLevel > 8:

            self.cookedString = "已经烤成木炭了"
        elif self.cookedLevel >5:

            self.cookedString = "熟了"
        elif self.cookedLevel >3:

            self.cookedString = "半熟半生"
        else:

            self.cookedString = " 还是生的"

    def addCondiments(self,condiments):
        self.condiments.append(condiments)
        # print(self.condiments)
    def __str__(self):
        return "烤红薯状态:%s%d,添加的饲料:%s"%(self.cookedString, self.cookedLevel, str(self.condiments))




potato = SweetPotato()

potato.cook(5)
print(potato.cookedString)
potato.addCondiments("番茄酱")
print(potato.condiments)
print(potato)









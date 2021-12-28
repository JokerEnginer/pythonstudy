# 定义一个家类
from Bed import Bed
class House():
    def __init__(self, area, info, addr):
        self.area = area
        self.info = info
        self.addr = addr
        self.usable_area = area
        self.containitems = []

    def __str__(self):
        msg  = "房子面积:%s;床的大小:%s ; 房子的可用面积:%s ;户型:%s; 地址:%s"%(self.area, "".join(self.containitems), self.usable_area, self.info, self.addr)
        msg += "  目前家里有的家具是:%s"%" ".join(self.containitems)
        return msg
    def add_items(self,items):
        self.usable_area -= items.get_area()
        self.containitems.append(items.get_name())

fang = House(123, "四房一厅", "广东深圳南山区")
print(fang)

bed1 = Bed("席梦思",4)
bed2 = Bed("木床",3)
fang.add_items(bed1)
fang.add_items(bed2)
print(bed1)
print(fang)

class Person(object):
    """定义人的类"""
    def __init__(self,name):
        super(Person, self).__init__()
        self.name = name
        self.hp = 100
        self.gun = None


    def load_bullet(self,dan_jia_temp, bullet_temp):
        # 定义装弹方法
        dan_jia_temp.baocun_bullet(bullet_temp)

    def install_danjia(self,gun_temp, dan_jia_temp):
        #定义安装弹夹方法
        gun_temp.baocun_danjia(dan_jia_temp)

    def nagun(self,gun_temp):
        """老王拿枪了"""
        self.gun = gun_temp

    def opengun(self,enemy_temp):
        """老王开枪"""
        self.gun.fire(enemy_temp)

    def diao_xue(self,power):
        self.hp -=power

    def __str__(self):
        if self.gun:
            return "%s的血量为%d, 他有一把%s"%(self.name, self.hp, self.gun)
        else:
            return "%s的血量为%d,他没有枪"%(self.name, self.hp,)


class Gun(object):
    """定义枪类"""
    def __init__(self,name):
        super(Gun, self).__init__()
        self.name = name  #记录枪的类型
        self.danjia = None

    def baocun_danjia(self,dan_jia_temp):
        #定义保存弹夹的方法
        self.danjia = dan_jia_temp

    def fire(self, enemy_temp):
        zidan_temp = self.danjia.tanchu_zidan()
        if zidan_temp:
            zidan_temp.dazhong(enemy_temp)
        else:
            print("弹夹没有子弹了...")


    def __str__(self):
        if self.danjia:
            return "枪的信息是%s,弹夹的信息为:%s"%(self.name, self.danjia)
        else:
            return "枪的信息是%s"%self.name

class DanJia(object):
    """定义弹夹类"""
    def __init__(self, max_nums):
        super(DanJia, self).__init__()
        self.max_nums = max_nums  #记录弹夹的最大子弹数
        self.bullet_list = []  #记录所有子弹的引用

    def baocun_bullet(self, bullet_temp):
        self.bullet_list.append(bullet_temp)

    def tanchu_zidan(self):
        if self.bullet_list:
            return  self.bullet_list.pop()
        else:
            return None

    def __str__(self):
        return "弹夹的信息:%d/%d"%(len(self.bullet_list), self.max_nums)
class Bullet(object):
    """定义子弹类"""
    def __init__(self,power):
        super(Bullet, self).__init__()
        self.power = power   #记录每颗子弹的伤害

    def dazhong(self,enemy_temp):
        enemy_temp.diao_xue(self.power)

def main():
    # 1.创建老王对象
    laowang = Person("laowang")

    # 2.创建枪类
    m4a1 = Gun("M4A1")

    # 3.创建弹夹类
    dan_jia = DanJia(30)

    #4.创建子弹类
    bullet = Bullet(10)

    #5.老王把子弹装到弹夹中
    laowang.load_bullet(dan_jia, bullet)

    #6.老王把弹夹装到枪中
    laowang.install_danjia(m4a1, dan_jia)

    #7.老王拿枪
    laowang.nagun(m4a1)

    # 测试弹夹信息
    print(dan_jia)
    # 测试枪的信息
    print(m4a1)
    # 测试老王的信息
    print(laowang)

    # 8创建敌人
    enemy = Person("隔壁老宋")
    print(enemy)

    # 9.老王开枪
    laowang.opengun(enemy)
    print(enemy)







if __name__ == '__main__':
    main()
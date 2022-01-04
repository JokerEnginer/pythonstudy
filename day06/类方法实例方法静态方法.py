class Game():
    num = 0
    # 实例方法
    def __init__(self):
        self.name = "zsr"


    # 类方法
    @classmethod
    def add_num(cls):
        cls.num = 100
     # 静态方法
    @staticmethod
    def print_info():
        print("---------------")
        print("-----游戏开始--")
        print("-----修改游戏角色--")
        print("---------------")


game = Game()
Game.add_num()   #通过类调用类方法
game.add_num()   #通过实例对象地调用类方法
print(Game.num)  #通过类调用类属性
Game.print_info()   #通过类调用静态方法
game.print_info()   #通过实例对象地调用静态方法




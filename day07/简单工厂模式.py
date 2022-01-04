class CarStore():

    def __init__(self):
        self.factory = FactoryCar()

    def order(self, car_type):
        return self.factory.car_select_type(car_type)

class FactoryCar():
    def car_select_type(self, car_type):
        if car_type == "奔驰E":
            return BenChi()
        elif car_type == "宝马":
            return Bmw()






class Car():
    def move(self):
        print("----正在行驶----")

    def music(self):
        print("----正在听音乐----")

    def stop(self):
        print("----要停车了----")

class BenChi(Car):
    def move(self):
        print("----奔驰E正在行驶----")

class Bmw(Car):
    def move(self):
        print("----宝马正在行驶----")

cs = CarStore()
car = cs.order("宝马")
car.move()
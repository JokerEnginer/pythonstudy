class CarStore(object):
    def order(self, car_type):
        return car_select_type(car_type)


def car_select_type(car_type):
    if car_type == "奔驰E":
        return BenChi()
    elif car_type == "宝马":
        return Bmw()



class Car():
    def move(self):
        print("---正在行驶---")

    def music(self):
        print("---正在听音乐---")

    def stop(self):
        print("---车辆停止---")

class BenChi(Car):
    def move(self):
        print("---我在开奔驰E---")

class Bmw(Car):
    pass


cs = CarStore()
car = cs.order("奔驰E")
car.move()

class Bed():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = "床的品牌是: %s; 床的大小: %s"%(self.name,self.area)
        return msg
    def get_name(self):
        return self.name

    def get_area(self):
        return self.area


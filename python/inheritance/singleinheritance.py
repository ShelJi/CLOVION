class cars:
    def __init__(self, brand):
        self.brand = brand
    def printData(self):
        print(self.brand)

class color(cars):
    def __init__(self, brand, color):
        super().__init__(brand)
        self.color = color
    def printData(self):
        print(self.brand, self.color)

car = color("audi", "green")
car.printData()
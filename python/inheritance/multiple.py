class cars:
    def __init__(self, brand, doors):
        self.brand = brand
        self.doors = doors
    def printData(self):
        print(self.brand)

class color(cars):
    def __init__(self, brand, doors, color):
        super().__init__(brand, doors)
        self.color = color
    def printData(self):
        print(self.brand, self.color, self.doors)

class tyres(color):
    def __init__(self, brand, doors, color, wheel):
        super().__init__(brand, doors, color)
        self.wheel = wheel
    def printData(self):
        print(f'car: {self.brand}, doors: {self.doors}, color: {self.color}, tyres: {self.wheel}')


car = tyres("audi", 4, "green", 4)
car.printData()
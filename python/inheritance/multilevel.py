class cars:
    def __init__(self, brand, doors):
        self.brand = brand
        self.doors = doors

class color:
    def __init__(self, colors):
        self.colors = colors

class tyres(cars, color):
    def __init__(self, brand, doors, colors, wheel):
        cars.__init__(self, brand, doors)
        color.__init__(self, colors)
        self.wheel = wheel
    def printData(self):
        print(f'car: {self.brand}, doors: {self.doors}, color: {self.colors}, tyres: {self.wheel}')


car = tyres("audi", "2", "green", 4)
car.printData()
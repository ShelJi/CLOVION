from icecream import ic


class cars:
    def __init__(self, brand: str, doors: int) -> None:
        self.brand = brand
        self.doors = doors
    def printData(self) -> None:
        ic(self.brand)

class color(cars):
    def __init__(self, brand: str, doors: int, color: str) -> None:
        super().__init__(brand, doors)
        self.color = color
    def printData(self) -> None:
        ic(self.brand, self.color, self.doors)

class tyres(color):
    def __init__(self, brand: str, doors: int, color: str, wheel: int) -> None:
        super().__init__(brand, doors, color)
        self.wheel = wheel
    def printData(self) -> None:
        # ic(f'car: {self.brand}, doors: {self.doors}, color: {self.color}, tyres: {self.wheel}')
        ic(self.brand, self.doors, self.color, self.wheel)

car = tyres("audi", 4, "green", 4)
car.printData()
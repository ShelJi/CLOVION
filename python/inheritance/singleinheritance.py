from icecream import ic


class cars:
    def __init__(self, brand: str) -> None:
        self.brand = brand
    def printData(self) -> None:
        ic(self.brand)

class color(cars):
    def __init__(self, brand: str, color: str) -> None:
        super().__init__(brand)
        self.color = color
    def printData(self) -> None:
        ic(self.brand, self.color)

car = color("audi", "green")
car1 = color("nissan", "blue")
# car2 = color()

# car.printData()
car1.printData()
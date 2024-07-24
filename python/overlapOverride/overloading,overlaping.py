# single inheritance
# overloading
class classs:
    def __init__ (self, name):
        self.name = name

    def printData(self):
        print(self.name)

class student(classs):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def printStudent(self):
        super().printData()
        print(self.id)

classs1 = student("hey", 1223)
classs1.printStudent()

# overlapping
class overLap(student):
    def __init__(self, name, id, phn):
        super().__init__(name, id)
        self.name = name
        self.id = id
        self.phn = phn
    def printData(self):
        print( self.name, self.id, self.phn)

classs2 = overLap("hello", 4456, 9876555555555)
classs2.printData()
from abc import ABC, abstractmethod # ABC - Abstract Base Class

class Vehicle(ABC): # abstract class should work oly for ABC inherited
# class Vehicle():
    @abstractmethod # Vehicle inherited class should have these functions to run
    def doors():
        pass
    
    @abstractmethod
    def wheels():
        pass
    
class Car(Vehicle):
    pass

class Bus(Vehicle):
    def doors(self):
        pass
    def wheels(self):
        pass

car1 = Car()

# op -> Exception has occurred: TypeError
# Can't instantiate abstract class Car without an implementation for abstract methods 'doors', 'wheels'
#   File "D:\CLOVION\python\inheritance\ABC-abstractclass.py", line 15, in <module>
#     car1 = Car()
#            ^^^^^
# TypeError: Can't instantiate abstract class Car without an implementation for abstract methods 'doors', 'wheels

bus1 = Bus()
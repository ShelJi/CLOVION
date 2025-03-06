# refer dunder or magic.png
# refer dunder or magic 2 .png.png

# __init__
# __str__

# __eq__
# __gt__
# __lt__

# __add__

# __contain__
# __getitem__

from icecream import ic


class Student:
    """To create a student data."""
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def print_data(self) -> None:
        ic(self.name, self.age)

    def __str__(self) -> str:
        return ic(self.name)


student1 = Student("jeberlin", 15)
student1.print_data()

print(student1)
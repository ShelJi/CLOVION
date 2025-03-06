from icecream import ic

class person:
    def __init__(self, name: str, age: int, id: int, company: str, job: str, school: str, clg: str) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.company = company
        self.job = job
        self.school = school
        self.clg = clg

        ic(self.name)
        ic(self.age)
        ic(self.id)
        ic("-----------")
    
    def employee(self) -> None:
        ic(self.company)
        ic(self.job)

    def eduction(self) -> None:
        ic(self.school)
        ic(self.clg)
        
        self.employee()

person1 = person("hello", 10, 1, "new", "worker", "shshh", "chh")
person2 = person("hello", 3, 5, "where", "kyaa", "somewhere", "eeee")

# person1.employee()
person1.eduction()
person2.eduction()
class person:
    def __init__(Self, name, age, id, company, job, school, clg):
        Self.name = name
        Self.age = age
        Self.id = id
        Self.company = company
        Self.job = job
        Self.school = school
        Self.clg = clg

        print(Self.name)
        print(Self.age)
        print(Self.id)
    
    def employee(Self):
        print(Self.company)
        print(Self.job)

    def eduction(Self):
        print(Self.school)
        print(Self.clg)

person1 = person("hello", 10, 1, "new", "worker", "shshh", "chh")
person1.employee()
person1.eduction()
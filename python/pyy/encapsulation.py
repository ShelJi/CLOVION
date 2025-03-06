class student:
    def __init__ (Self ,name, id, age, std):
        Self.name = name
        Self.id = id
        Self.age = age
        Self.std = std
        
    def printing(Self):
        print("")
        print(f"Name is {Self.name}")
        print(f"ID is {Self.id}")
        print(f"Age is {Self.age}")
        print(f"STD id {Self.std}")
        print("")

student1 = student("hello", 12, 21, "wow")
student2 = student("world", 1, 31, "new")

student1.printing()
student2.printing()
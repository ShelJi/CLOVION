# name = "jebin"
# course = "django" # django - 6, php - 3, UI/UX - 2, Flutter - 5
# course_period = 3

# # print(name)
# # print(course)
# # print(course_period)

# # class CourseCenter:
# #     def __init__(self):
# #         print("Class CAlled")

# #     def print_hello(self):
# #         print("Hello World!")

# # student1 = CourseCenter()







class CourseCenter:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.course_period = 0
        self.student()

    def course_selection(self):
        if self.course == "django":
            self.course_period = 6

        elif self.course == "php":
            self.course_period = 3

    def student(self):
        self.course_selection()


studen1 = CourseCenter("jebin", "django")
studen2 = CourseCenter("joe", "php")


print(studen2.name)
print(studen2.course)
print(studen2.course_period)

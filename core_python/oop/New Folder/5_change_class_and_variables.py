class Student:
    name = "Abdul Zoha" #class_variable

    def __init__(self):
        self.age = 28
    def details(self):
        gender = "male"
s = Student()

"""Before changing"""
print(f"Class_variable: {Student.__dict__}")
print()
print(f"Instance_variable: {s.__dict__}")
print()
print(f"Variable of instance method: {Student.details.__dict__}")

"""changing variables"""
# Student.name = "Tabassum Khatoon"
# s.age = 21
# Student.details.gender = "female"

"""After changing"""
# print(f"Class_variable: {Student.__dict__}")
# print()
# print(f"Instance_variable: {s.__dict__}")
# print()
# print(f"Variable of instance method: {Student.details.__dict__}")
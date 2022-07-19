class Student:
    pass
    def __init__(self):
        pass
    def details(self):
        pass
s = Student() #making instance

"""making variable"""
Student.name = "Abdul Zoha" #class_variable
s.age = 28 #instance_variable
Student.details.gender = "male" #variable of instance method

print(f"Class_variable: {Student.__dict__}")
print()
print(f"Instance_variable: {s.__dict__}")
print()
print(f"Variable of instance method: {Student.details.__dict__}")
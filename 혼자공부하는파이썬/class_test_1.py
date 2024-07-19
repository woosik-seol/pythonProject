from typing import *

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ":" + str(self.age)

student1 = Student("이름1", 1)
student2 = Student("이름2", 2)

print(student1)
# 이름1:1

print(str(student2))
# 이름2:2

print(isinstance(student2, Student))
# True
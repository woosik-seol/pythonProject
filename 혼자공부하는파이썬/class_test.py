from typing import *


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + str(self.age)


class ClassRoom:
    # 클래스 변수

    count = 0
    students: List[Student] = []

    @classmethod
    def add_student(cls, student: Student):
        cls.students.append(student)

    @classmethod
    def print(cls):
        for student in cls.students:
            print(student)

    @staticmethod
    def calculate_average(korean, english, math):
        return (korean + english + math) / 3

student1 = Student("이름1", 1)
student2 = Student("이름2", 2)

ClassRoom.add_student(student1)
ClassRoom.add_student(student2)

ClassRoom.print()
# 이름11
# 이름22

print(ClassRoom.calculate_average(80,90,100))
# 90.0
from dataclasses import dataclass
from typing import *

@dataclass
class Student:
    name: str = ""
    age: int = 0

class ClassRoom:
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

# class_room = ClassRoom()

student1 = Student("이름1", 1)
student2 = Student("이름2", 2)

ClassRoom.add_student(student1)
ClassRoom.add_student(student2)

ClassRoom.print()
# Student(name='이름1', age=1)
# Student(name='이름2', age=2)

print(ClassRoom.calculate_average(80,90,100))
# 90.0
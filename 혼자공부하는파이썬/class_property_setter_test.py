class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age cannot be negative")
        self._age = age

student = Student("이름1", 1)

print(student.name)
print(student.age)
# 이름1
# 1

student.name = "이름2"
student.age = 2

print(student.name)
print(student.age)
# 이름2
# 2

print(student)
# <__main__.Student object at 0x10340ade0>




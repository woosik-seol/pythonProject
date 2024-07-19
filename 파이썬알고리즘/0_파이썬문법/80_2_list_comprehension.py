# 리스트 컴프리헨션

output = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(output)
# [2, 6, 10, 14, 18]


#Generator

def get_natural_number():
    n = 0
    while True:
        yield n
        n = n + 1

g = get_natural_number()

for _ in range(0, 5):
    print(next(g))
# 0
# 1
# 2
# 3
# 4


# enumerate
# - list, set, tuple
# => 인덱스를 포함한 enumerate 객체로 리턴

a = [1,2,45]
print(enumerate(a))
# <enumerate object at 0x103131e40>
print(list(enumerate(a)))
# [(0, 1), (1, 2), (2, 45)]


# 나눗셈 연산자

print(5 / 3)
# 1.6666666666666667

print(5 // 3)
# 1

print(5 % 3)
# 2

print(divmod(5, 3))
# (1, 2)


# print

print('A1', 'B2')
# A1 B2

print('A1', 'B2', sep=',')
# A1,B2

a = ['A', 'B']
print(" ".join(a))
# A B

a = ('A', 'B')
print(" ".join(a))
# A B


# f-string
# - formatted string literal

idx = 1
fruit = 'Apple'
print(f"{idx}: {fruit}")
# 1: Apple


# 파이썬 주요 자료형

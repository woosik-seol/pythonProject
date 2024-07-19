# 객체복사
# - 모든 것이 객체 (파이썬의 중요한 특징)
# - 숫자, 문자 까지도 모두 객체

import copy
a = [1, 2, 3]
# 참조가 되지 않도록 값 자체를 복사하려면
a[:]
a.copy()
copy.deepcopy(a)

a = "strawberry"
b = "strawberry"
c = 1
d = 1
e = copy.deepcopy(c)

print(id(a)) # 4381810544
print(id(b)) # 4381810544
print(id(c)) # 4379120736
print(id(d)) # 4379120736
print(id(e)) # 4379120736

a = [[1, 2], 3]
b = a
c = a[:]
d = a.copy()
e = copy.deepcopy(a)

print(id(a)) # 4305963328
print(id(b)) # 4305963328
print(id(c)) # 4306696768
print(id(d)) # 4306648256
print(id(e)) # 4306648128

print(id(a[0])) # 4305965120
print(id(b[0])) # 4305965120
print(id(c[0])) # 4305965120
print(id(d[0])) # 4305965120
print(id(e[0])) # 4306648192


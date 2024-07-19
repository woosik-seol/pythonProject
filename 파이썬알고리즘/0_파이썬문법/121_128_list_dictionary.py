# 리스트

a = list([2,1]) # a = []

a.sort()
a.reverse()

i = 1
del a[i]

element = 5
a.append(element)
a.pop(0)
a.pop()
a[:]

try:
    print(a[9])
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("success")
finally:
    print("close if there is something opened..")


# 딕셔너리

a = dict() # a = {}
a['key3'] = 'value3'
print(a['key3'])
# value3

for k, v in a.items():
    print(k, v)

if 'key3' in a:
    del a['key3']


# defaultdict 객체
# - 존재하지 않는 키를 조회할 경우,
# - 해당 키에 대한 아이템을 생성

import collections
a = collections.defaultdict(int)

a['c'] += 1


# Counter 객체

import collections
a = [1,2,3,4,5,5,5,6,6]
b = collections.Counter(a)
print(b.most_common(2))
# [(5, 3), (6, 2)]


# OrderedDict 객체
# - 입력 순서가 유지
# - 파이썬 3.7 부터는 사용할 필요가 없어짐
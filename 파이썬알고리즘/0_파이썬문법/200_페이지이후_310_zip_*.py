# zip 함수 p310

a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]

print(zip(a,b,c))
# <zip object at 0x104d7db80>
print(list(zip(a,b,c)))
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]


# 아스터리스크 asterisk *
# - 시퀀스를 풀어헤치는 연산자
# - sequence unpacking operator

nums = [1,2,3,4,5,5,5,6,6]
import collections
result = collections.Counter(nums).most_common(2)
print(result)
# [(5, 3), (6, 2)]

result = list(zip(*collections.Counter(nums).most_common(2)))
print(result)
# [(5, 6), (3, 2)]
# * 으로 언패킹을 해줘야 튜플을 풀 수 있다

fruit = ['lemon', 'pear', 'watermelon', 'tomato']
for f in fruit:
    print(f, end=' ')
print(*fruit)
# lemon pear watermelon tomato lemon pear watermelon tomato

a, *b = [1,2,3,4]
print(a)
# 1
print(b)
# [2, 3, 4]

*a, b = [1,2,3,4]
print(a)
# [1, 2, 3]
print(b)
# 4

# * 1개는 튜플 또는 리스트 등의 시퀀스 언패킹
# * 2개는 키/값 페어를 언패킹

date_info = {'year': '2020', 'month': '01', 'day': '7'}
new_info = {**date_info, 'day':14}
print(new_info)
# {'year': '2020', 'month': '01', 'day': 14}

# map() function
# map(func, iter)

# 1
def addition(n):
    return n + n

numbers = (1,2,3,4)
result = map(addition, numbers)
print(result)
# <map object at 0x1031d81c0>
print(list(result))
# [2, 4, 6, 8]

numbers = (1,2,3,4)
result = map(lambda x: x + x, numbers)
print(list(result))
# [2, 4, 6, 8]

numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x,y: x + y, numbers1, numbers2)
print(list(result))
# [5, 7, 9]
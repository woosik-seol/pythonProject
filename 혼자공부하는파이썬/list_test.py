list_a = [1,2,3,4]

del list_a[2]
print(list_a)
# [1, 2, 4]

del list_a[:]
print(list_a)
# []

print(5 in list_a)
# False

dictionary = {}
print(dictionary.get('key'))
# None

print(reversed(range(5)))
# <range_iterator object at 0x10342a340>

list_a = ["23","2","3","4"]
print("".join(list_a))
# 23234

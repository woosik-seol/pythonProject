

def yield_test():
    counter = 0

    while True:
        counter += 1
        yield counter

func = yield_test()

print(next(func))
print(next(func))
print(next(func))

# 1
# 2
# 3


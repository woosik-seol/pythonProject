input = [1,2,3]
output = []

def permutation(path=[]):
    if len(path) == len(input):
        output.append(path[:])
        return
    for i in input:
        if i not in path:
            path.append(i)
            permutation(path)
            path.pop()

permutation([])
print(output)

origin_input = [1,2,3]
input = origin_input[:]
output = []

def permutation(path=[], input=[]):
    if len(path) == len(origin_input):
        output.append(path[:])
        return
    for i, num in enumerate(input):
        del input[i]
        path.append(num)
        permutation(path, input)
        path.pop()
        input.insert(i, num)

permutation([], input)
print(output)


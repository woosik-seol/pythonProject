nums = [1,2,3]
output = []

def subsets(nums=[]):
    if nums not in output:
        output.append(nums[:])
    for i, num in enumerate(nums):
        nums.pop(i)
        subsets(nums)
        nums.insert(i, num)

subsets(nums)
print(output)


nums = [1,2,3]
output = []

def dfs(depth=0, path=[]):
    if depth == len(nums):
        output.append(path[:])
        return

    dfs(depth+1, path)

    path.append(nums[depth])
    dfs(depth+1, path)
    path.pop()

dfs(0, [])
print(output)


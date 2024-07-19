
#
# https://www.youtube.com/watch?v=CJ4BTaGjNMs

# Interview 1: Coding Interview (60 mins)
# Coding
# Systems Design
# Troubleshooting
# AI/ML
# Data Analysis

# 커뮤니케이션과 창의성
# Cases
# Exception (문제 영역을 제한하다)


# exception: not 0 or not 1
# 모듈로 전환


# 0:      1:      2:      3:      4:      5:      9:      11:     12:
# - 1     - 1     -0      -0      -0      -1      -0      -0      -0
# - 0     - 0     -1      -2      -3      -0      -1      -3      -4
# - 0     - 0     -1      -2      -3      -3      -3      -3      -4
#
# index:
# - source
# - count
# - outout

def count_longest_0(source="1100011010000"):
    # source = "1100011010000"
    outout = 0
    count = 0

    for i, item in enumerate(source):
        if item == '0':
            count += 1
            outout = max(outout, count)
        else:
            count = 0
        # elif item == '1':
        #     count = 0
        # else:
        #     raise Exception("Neither 0 nor 1")

    return outout


print(count_longest_0("11000110100000"))


def count_longest_0(source="1100011010000"):
    # source = "1100011010000"
    outout = 0
    count = 0

    for i in range(len(source)):
        if source[i] == '0':
            count += 1
            outout = max(outout, count)
        else:
            count = 0
        # elif item == '1':
        #     count = 0
        # else:
        #     raise Exception("Neither 0 nor 1")

    return outout


print(count_longest_0("11000110100000"))










# 틀렸음. 마지막 문자
def test():
    source = "1100011010000"
    print("asdfsad")
    outout = 0
    count = 0
    for i, char in enumerate(source):
        if char == '0':
            count += 1
        else:
            outout = max(outout, count)
            count = 0
    print(outout)
    print("asdfsad")

# 틀렸음. 마지막 문자
def test2():
    source = "11000110100000"
    print("asdfsad")
    outout = 0
    count = 0
    for i in range(len(source)):
        if source[i] == '0':
            count += 1
        else:
            outout = max(outout, count)
            count = 0
    print(outout)
    print("asdfsad")

# test()
# test2()







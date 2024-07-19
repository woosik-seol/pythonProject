import datetime

def main():
    now = datetime.datetime.now()

    print(now)
    print(type(now))

    print(now.year)
    print(now.month)
    print(now.day)

    print(now.hour)
    print(now.minute)
    print(now.second)

    print(str(2323.23))

if __name__ == "__main__":
    main()

# 2024-07-07 12:09:58.005715
# <class 'datetime.datetime'>
# 2024
# 7
# 7
# 12
# 9
# 58
# 2323.23
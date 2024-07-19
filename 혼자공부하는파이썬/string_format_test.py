def main():
    a = "{}asdf".format(4)
    b = "{} {} ".format("sdbs", 45)
    c = "{:010d}{:05d}".format(45, 2356)
    d = "{:010d}{:05d}".format(-45, 2356)

    print(a)
    print(b)
    print(c)
    print(d)

# 4asdf
# sdbs 45
# 000000004502356
# -00000004502356


if __name__ == "__main__":
    main()
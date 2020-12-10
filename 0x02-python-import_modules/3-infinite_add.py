#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    i = 1
    total = 0
    while i < count:
        total += int(sys.argv[i])
        i += 1
    print("{}".format(total))

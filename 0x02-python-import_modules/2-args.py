#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    i = 0
    while i <= count:
        if count == 0:
            print("{} arguments.".format(count))
            break
        if count == 1 and i == 0:
            print("{} argument:".format(count))
            i += 1
            continue
        if count > 1 and i == 0:
            print("{} arguments:".format(count))
            i += 1
            continue
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

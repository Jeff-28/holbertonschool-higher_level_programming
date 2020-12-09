#!/usr/bin/python3


def uppercase(str):
    for i in str:
        letter = ord(i)
        if i.islower():
            letter -= 32
        print("{:c}".format(letter), end="")

    print()

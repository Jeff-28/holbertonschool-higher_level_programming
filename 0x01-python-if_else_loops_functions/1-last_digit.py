#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    negative = number * -1
    last = negative % 10
else:
    last = number % 10

print("Last digit of {} is ".format(number), end="")
if last == 0:
    print("{} and is 0".format(last))
if last > 5:
    print("{} and is greater than 5".format(last))
if last < 6 and last != 0:
    print("{} and is less than 6 and not 0".format(last))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    negative = number * -1
    last = negative % 10

else:
    last = number % 10

if last == 0:
    print("Last digit of 0 is 0 and is 0")

if last > 5:
    print("Last digit of", number, "is", last, "and is greater than 5")

if last < 6 and last != 0:
    print("Last digit of", number, "is", last, "and is less than 6 and not 0")

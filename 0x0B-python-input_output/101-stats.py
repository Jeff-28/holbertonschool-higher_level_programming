#!/usr/bin/python3
"""
I/O Module
"""

import sys


line_dict = {}
count = 0
total_size = 0
try:
    for line in sys.stdin:
        strings = line.split()
        status = strings[-2]
        total_size += int(strings[-1])
        count += 1
        if status not in line_dict.keys():
            line_dict[status] = 1
        else:
            line_dict[status] += 1
        if count == 10:
            print("File size: {}".format(total_size))
            ordered = sorted(line_dict.keys())
            for key in ordered:
                print("{}: {}".format(key, line_dict[key]))
            count = 0

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key in ordered:
        print("{}: {}".format(key, line_dict[key]))

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
        if len(strings) >= 2:
            status = strings[-2]
            x = count
            if status in line_dict:
                line_dict[status] += 1
                count += 1
            else:
                line_dict[status] = 1
                count += 1
            try:
                total_size += int(strings[-1])
                if x == count:
                    count += 1
            except:
                if x == count:
                    continue
        if count % 10 == 0:
            print("File size: {}".format(total_size))
            ordered = sorted(line_dict.keys())
            for key in ordered:
                print("{}: {}".format(key, line_dict[key]))
    print("File size: {}".format(total_size))
    for key in ordered:
        print("{}: {}".format(key, line_dict[key]))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key in ordered:
        print("{}: {}".format(key, line_dict[key]))

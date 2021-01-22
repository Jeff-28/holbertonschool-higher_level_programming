#!/usr/bin/python3
"""
I/O Module
"""

import sys


line_dict = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
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
            try:
                total_size += int(strings[-1])
                if x == count:
                    count += 1
            except:
                if x == count:
                    continue
        if count % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in sorted(line_dict.items()):
                if value:
                    print("{}: {}".format(key, value))
    print("File size: {}".format(total_size))
    for key, value in sorted(line_dict.items()):
        if value:
            print("{}: {}".format(key, value))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key, value in sorted(line_dict.items()):
        if value:
            print("{}: {}".format(key, value))

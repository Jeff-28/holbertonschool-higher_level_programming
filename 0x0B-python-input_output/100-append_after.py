#!/usr/bin/python3
"""
I/O Module
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string"""

    with open(filename, "r", encoding="utf-8") as myfile:
        mylist = []
        while True:
            line = myfile.readline()
            if line == "":
                break
            mylist.append(line)
            if search_string in line:
                mylist.append(new_string)
    with open(filename, 'w', encoding='utf-8') as myfile:
        myfile.writelines(mylist)

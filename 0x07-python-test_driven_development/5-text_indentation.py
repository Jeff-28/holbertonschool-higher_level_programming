#!/usr/bin/python3
"""
Text Module
"""


def text_indentation(text):
    """
    Formats text.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    separators = ['.', '?', ':']
    text.strip()
    for i in range(len(text)):
        if (text[i] == " ") and (text[i - 1] in separators):
            continue
        print(text[i], end="")
        if text[i] in separators:
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1

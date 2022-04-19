"""
algorithms.py
"""


def read_data(filename):
    infile = open(filename, "r")
    words = infile.read()
    words2 = words.replace("\n", " ")
    mylist = words2.split(" ")
    return mylist


def is_in_linear(search_val, values):
    i = 0
    while i < len(values) and search_val != values[i]:
        i = i + 1
    return i < len(values)

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


def is_in_binary(search_val, values):
    lindex = 0
    rindex = len(values) - 1
    while lindex <= rindex:
        mindex = (lindex + rindex) // 2
        mvalue = values[mindex]
        if mvalue == search_val:
            return mindex
        elif mvalue < search_val:
            lindex = mindex + 1
        else:
            rindex = mindex - 1
    return -1


def selection_sort(values):
    for i in range(len(values)):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[min_index] > values[j]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
    return values


def calc_area(rect):
    topleft = rect.getP1()
    bttmright = rect.getP2()
    width = (topleft.getX() - bttmright.getX())
    height = (topleft.getY() - bttmright.getY())
    area = width * height
    return area


def rect_sort(rectangles):
    areas = []
    for rectangle in rectangles:
        each_area = calc_area(rectangle)
        areas.append(each_area)
    areas_sorted = selection_sort(areas)
    return areas_sorted


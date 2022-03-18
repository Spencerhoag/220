"""
Name: <Spencer Hoag>
<hw8>.py

Problem: <>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    total = 0
    for number in nums:
        total = total + number
    return total


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])
        if abs(float(nums[i])) % 1 == 0:
            int(nums[i])
        else:
            float(nums[i])


def sum_of_squares(nums):
    mylist = []
    for i in nums:
        list_split = i.split(",")
        to_numbers(list_split)
        square_each(list_split)
        ans = sum_list(list_split)
        mylist.append(ans)
    return mylist


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5 or weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX()-circumference_point2.getX())**2+(center2.getY()-circumference_point2.getY())**2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("yellow")
    circle_two.draw(win)
    if did_overlap(circle_one, circle_two):
        overlap_msg = Text(Point(5, 5), "The Circles Overlap.")
        overlap_msg.draw(win)
    else:
        no_overlap_msg = Text(Point(5, 5), "The Circles Do Not Overlap.")
        no_overlap_msg.draw(win)
    msg = Text(Point(5, 8), "Click Anywhere to Close Window.")
    msg.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()
    center1x = center1.getX()
    center1y = center1.getY()
    center2x = center2.getX()
    center2y = center2.getY()
    radius1 = circle_one.getRadius()
    radius2 = circle_two.getRadius()
    dist = math.sqrt((center2x - center1x) ** 2 + (center2y - center1y) ** 2)
    radsum = radius1 + radius2
    if dist >= radsum:
        return True
    else:
        return False


if __name__ == '__main__':
    sum_of_squares(["1, 4.5, 2"])

"""
Name: <Spencer Hoag>
<hw6>.py

Problem: <The first program takes user input as a float and outputs it as a dollar value by
 formatting two decimal places into the input. The second program takes user input for a message
 and a key value, then iterates through every letter in the message and adds the integer value
 of the key to the ordinance value of each letter, then outputs the new ordinance values as characters.
 The third and fourth functions calculate the SA and volume of a sphere by initializing the arithmetic
 to each variable, then returning the corresponding variable. The fifth function calculates the sum of
 the first n natural numbers by looping through the range of the given number starting at 1, then
 adding each term in the range to an accumulator and outputting that sum. The sixth function does the
 exact same thing, but cubes each number in the range of the given number.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math


def cash_converter():
    user_input = float(input("enter an integer: "))
    print("That is ${:.2f}".format(user_input))


def encode():
    msg = input("enter a message: ")
    key = input("enter a key: ")
    nums = ""
    for letter in msg:
        key_chr = ord(letter) + int(key)
        nums = nums + str(chr(key_chr))
    print(nums, end="")


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    print("Surface Area is: ", area)
    return area


# radius = float(input("Enter the radius: "))
# sphere_area(radius)


def sphere_volume(radius):
    vol = (4 / 3) * math.pi * radius ** 3
    print("Volume is: ", vol)
    return vol


# radius = float(input("Enter the radius: "))
# sphere_volume(radius)


def sum_n(number):
    my_sum = 0
    for i in range(1, number + 1):
        my_sum = my_sum + i
    print(my_sum)
    return my_sum


# number = int(input("Enter a number: "))
# sum_n(number)


def sum_n_cubes(number):
    my_sum = 0
    for i in range(1, number + 1):
        my_sum = my_sum + i * i * i
    print(my_sum)
    return my_sum


# number = int(input("Enter a number: "))
# sum_n_cubes(number)


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

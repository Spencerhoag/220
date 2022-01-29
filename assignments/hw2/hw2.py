"""
Name: <Spencer Hoag>
<hw2>.py

Problem: <The first program uses a for loop ranging up to the user's input, every value that's remainder equals 0 is
added together and displayed. The second program uses a series of for loops to display a table of numbers, the third
takes the user's input of the length of each side and imports the math.sqrt operation to display the area. The final
two use for loops to display the user's input as a sum of squares and the power of numbers.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""



def sum_of_threes():
    bound = eval(input("What is the upper bound? "))
    total = 0
    for _ in range(0, bound + 1):
        if _ % 3 == 0:
            total = total + _
    print("Sum of threes is: ", total)

def multiplication_table():
    for _ in range(1, 11):
        print(_, end="\t")
    print()
    for i in range(2, 21, 2):
        print(i, end="\t")
    print()
    for j in range(3, 31, 3):
        print(j, end="\t")
    print()
    for k in range(4, 41, 4):
        print(k, end="\t")
    print()
    for _l in range(5, 51, 5):
        print(_l, end="\t")
    print()
    for m in range(6, 61, 6):
        print(m, end="\t")
    print()
    for n in range(7, 71, 7):
        print(n, end="\t")
    print()
    for o in range(8, 81, 8):
        print(o, end="\t")
    print()
    for p in range(9, 91, 9):
        print(p, end="\t")
    print()
    for q in range(10, 101, 10):
        print(q, end="\t")

def triangle_area():
    import math
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("Enter side c length: "))
    variable_s = (side_a + side_b + side_c) / 2
    draft_area = variable_s * (variable_s - side_a) * (variable_s - side_b) * (variable_s - side_c)
    area = math.sqrt(draft_area)
    print("Area is: ", area)

def sum_squares():
    lo_range = eval(input("Enter lower range: "))
    up_range = eval(input("Enter upper range: "))
    square = 0
    for _ in range(lo_range, up_range + 1):
        square = square + (_ * _)
    print(square)

def power():
    base = eval(input("Enter base: "))
    exp = eval(input("Enter exponent: "))
    result = 1
    for _ in range(exp):
        result = result * base
    print(base, "^", exp, "=", result)

if __name__ == '__main__':
    pass

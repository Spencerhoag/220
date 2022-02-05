"""
Name: <Spencer Hoag>
<hw3>.py

Problem: <All programs use for loops to obtain user input and display the average grade of students, the total amount
tipped across five people, the square root of a number, and a sequence with steps by 2 and repeats every number twice,>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    total_grades = eval(input("How many grades will you enter? "))
    acc = 0
    avg = 0
    for _ in range(total_grades):
        acc = eval(input("Enter grade: "))
        avg = avg + acc / total_grades
    print("Average is:", avg)


def tip_jar():
    total = 0
    for _ in range(5):
        tip = eval(input("How much would you like to donate? "))
        total = total + tip
    print("Total tips: ", total)


def newton():
    root = eval(input("What number do you want to square root? "))
    improve = eval(input("How many times should we improve the approximation? "))
    approx = 1
    for _ in range(improve):
        approx = (approx + root / approx) / 2
    print("The square root is approximately", approx)


def sequence():
    terms = eval(input("How many terms would you like? "))
    for _ in range(1, terms + 1, 2):
        for i in range(2):
            print(_, end="\t")


def pi():
    terms = eval(input("How many terms in the series? "))
    acc = 1




if __name__ == '__main__':
    pass

"""
Name: <Spencer Hoag>
<hw1>.py

Problem: <All lines of code are intended to take the user input and use it to calculate and display
the area of a rectangle, volume, a basketball player's shooting percentage, a customer's total cost
of shipped coffee, and the conversion from kilometers to miles.>
Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)
def shooting_percentage():
    fgm = eval(input("Enter the player's total shots: "))
    fga = eval(input("Enter how many shots the player made: "))
    fgp = (fgm / fga) * 100
    print("Shooting Percentage: ", fgp, "%")
def coffee():
    pounds_ordered = eval(input("How many pounds of coffee would you like? "))
    cost_per_pound = 10.50
    shipping = 0.86
    order_fee = 1.50
    total_cost = (pounds_ordered * cost_per_pound) + (shipping * pounds_ordered) + order_fee
    print("You're total is: ", total_cost)
def kilometers_to_miles():
    km = eval(input("How many Kilometers did you travel? "))
    miles = km * 0.62137
    print("That's", miles, "miles!")
if __name__ == '__main__':
    pass

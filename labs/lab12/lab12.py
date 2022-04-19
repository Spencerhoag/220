"""
lab12.py
"""
from random import randint


def find_and_remove_first(alist, value):
    alist.insert(value, "Spencer")
    alist.remove(value)


def good_input():
    user_input = eval(input("Enter a number between 1-10: "))
    while user_input < 1 or user_input > 10:
        user_input = eval(input("The number entered is not in range, please enter a number between 1-10: "))
    return user_input


def num_digits():
    user_input = eval(input("Enter a positive integer: "))
    while user_input > 0:
        i = 0
        while user_input > 0:
            user_input = user_input // 10
            i = i + 1
        print("Number has {} digits".format(i))
        user_input = eval(input("Enter a positive integer: "))


def hi_lo_game():
    ran_num = randint(1, 100)
    print(ran_num)
    i = 1
    while i < 8:
        guess = eval(input("Enter a number to guess: "))
        if guess == ran_num:
            print("You won in {} guesses!".format(i))
            i = i + 9
        elif guess > ran_num:
            print("Guess is too high")
            i = i + 1
        elif guess < ran_num:
            print("Guess is too low")
            i = i + 1
    if i == 8:
        print("Sorry, you lose. The number was {}".format(ran_num))


if __name__ == "__main__":
    pass

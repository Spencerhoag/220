"""
lab13.py
"""


def trade_alert(filename):
    infile = open(filename, "r")
    nums = infile.read()
    nums_list = nums.split(" ")
    for num in nums_list:
        if int(num) > 830:
            print("Warning --Occurred at {} Seconds--".format(nums_list.index(num) + 1))
        elif int(num) == 500:
            print("Pay Attention --Occurred at {} Seconds--".format(nums_list.index(num) + 1))
    infile.close()

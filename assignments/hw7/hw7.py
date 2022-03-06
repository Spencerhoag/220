"""
Name: <Spencer Hoag>
<hw7>.py

Problem: <The first function reads the content of one file line by line and uses a for loop to iterate
through each word in every line, then prints the index value of each word and the actual word to the
another file each on a new line. The second function also outputs data to another file line by line
using a for loop, but splits each line by the spaces and uses the index value of each word to print
the names and total wages of employees to another file. The third function removes every hash mark in
the inputted isbn then uses a list ranging from 10-1 to multiply the corresponding index values of the
 isbn and list, then sums the products up and returns that total. The fourth function reads the content
of a file and prints the data to another file which has the name of an inputted string by using the
format method. The fifth function does the same thing as the fourth, but reads the file line by line
and calls on a previous encode function to encrypt each line and print it to another file. The last
function also does the same as the previous two, but calls on the encode_better function to encrypt each
line and uses the content of another text file as the key, and prints the encrypted data to another file.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    words = in_file.readlines()
    line_join = " ".join(words)
    word_list = line_join.split(" ")
    for word in range(len(word_list)):
        print(word + 1, end=" ", file=out_file)
        print(word_list[word].rstrip("\n"), file=out_file)
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    for data in in_file:
        line = data.split(" ")
        bonus = int(line[3]) * 1.65
        wage = float(line[2]) * int(line[3]) + bonus
        print(line[0], line[1], "{:.2f}".format(wage), file=out_file)
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    no_hash_isbn = isbn.replace("-", "")
    total = 0
    check_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    num1 = int(no_hash_isbn[0]) * check_list[0]
    num2 = int(no_hash_isbn[1]) * check_list[1]
    num3 = int(no_hash_isbn[2]) * check_list[2]
    num4 = int(no_hash_isbn[3]) * check_list[3]
    num5 = int(no_hash_isbn[4]) * check_list[4]
    num6 = int(no_hash_isbn[5]) * check_list[5]
    num7 = int(no_hash_isbn[6]) * check_list[6]
    num8 = int(no_hash_isbn[7]) * check_list[7]
    num9 = int(no_hash_isbn[8]) * check_list[8]
    num0 = int(no_hash_isbn[9]) * check_list[9]
    total = total + num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num0
    return total


def send_message(file_name, friend_name):
    in_file = open(file_name, "r")
    out_file = open("{}.txt".format(friend_name), "w")
    data = in_file.read()
    print(data.rstrip('\n'), file=out_file)
    in_file.close()
    out_file.close()


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, "r")
    out_file = open("{}.txt".format(friend_name), "w")
    data = in_file.readlines()
    data_ = "".join(data)
    output = ""
    for words in data_:
        output = output + encode(words, key)
    print(output[:-1], file=out_file)
    in_file.close()
    out_file.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file = open(file_name, "r")
    out_file = open("{}.txt".format(friend_name), "w")
    pad_file = open(pad_file_name, "r")
    msg = in_file.read()
    pad = pad_file.read()
    output = encode_better(msg, pad)
    print(output.rstrip("\n"), file=out_file)
    in_file.close()
    out_file.close()


if __name__ == '__main__':
    pass

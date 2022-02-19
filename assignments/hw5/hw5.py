"""
Name: <Spencer Hoag>
<Hw5>.py

Problem: <The first program takes user input of a full name, splits the string into a list that
separates each element followed by a space, then prints last name first, followed by the first.
The second program takes the user input of a website domain and splits it into a list with
each element separated by a ".", forcing every domain to have elements ranging from index
 values 0-2, in which the program prints the first index value which is always the name.
 The third program creates a for loop ranging from a user input of how many students there
 are, then asks the name for each student and prints the initials of each student by taking
  the index value 0, which is always the first letter of each name. The fifth program loops
  through the total amount of sentences inputted by the user, and prints the third letter
  in each sentence by slicing each one from the start, stepping by 3. The sixth program
prints the average length of all words in a user inputted sentence by splitting the string
  and using len() to calculate the length of the sentence and each letter in every word. The
last program >

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    input_name = input("enter a name (first last): ")
    list_name = input_name.split(" ")
    print(list_name[1] + "," + " " + list_name[0])


def company_name():
    domain = input("enter a domain: ")
    name = domain.split(".")
    print(name[1])


def initials():
    total_kids = eval(input("how many students are in the class?"))
    for i in range(1, total_kids + 1):
        print("what is the name of student", str(i) + "?", end="")
        name = input(" ")
        initial = name.split(" ")
        initial_1 = initial[0]
        initial_2 = initial[1]
        print(initial_1[0].capitalize() + initial_2[0].capitalize())


def names():
    pass


def thirds():
    total_sent = eval(input("Enter the number of sentences: "))
    total = []
    for i in range(1, total_sent + 1):
        print("enter sentence", str(i) + ":", end="")
        each_sent = input(" ")
        third_letter = each_sent[0::3]
        total.append(third_letter)
    print("\n".join(total))


def word_average():
    sent = input("enter a sentence: ")
    list_sent = sent.split(" ")
    acc = 0
    for i in list_sent:
        character = len(i)
        acc = acc + character
    avg = acc / (len(list_sent))
    print(avg)


def pig_latin():
    sent = input("enter a sentence to convert to pig latin: ")
    list_sent = sent.split(" ")
    for i in list_sent:
        pig_latin_ = (i[1:] + i[:1] + "ay")
        print(pig_latin_.lower(), end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass

"""
hw9.py
"""
from random import randint
from graphics import GraphWin, Point, Circle, Line, Text, Entry


def get_words(file_name):
    in_file = open(file_name, "r")
    mylist = []
    for words in in_file.readlines():
        mylist.append(words)
    return mylist


def get_random_word(words):
    ran_index = randint(0, len(words) - 1)
    ran_num = words[ran_index]
    return ran_num.strip()


def letter_in_secret_word(letter, secret_word):
    return secret_word.find(letter) != -1


def already_guessed(letter, guesses):
    return letter in guesses


def make_hidden_secret(secret_word, guesses):
    blanks = "_" * len(secret_word)
    for letter in range(len(secret_word)):
        if secret_word[letter] in guesses:
            blanks = blanks[:letter] + secret_word[letter] + blanks[letter + 1:]
    spaced = " ".join(blanks)
    return spaced


def won(guessed):
    return guessed.find("_") == -1


def play_graphics(secret_word):
    win = GraphWin("Hangman", 800, 800)
    win.setBackground("white")
    bttm = Line(Point(350, 500), Point(450, 500))
    bttm.draw(win)
    vert = Line(Point(400, 500), Point(400, 250))
    vert.draw(win)
    top = Line(Point(400, 250), Point(300, 250))
    top.draw(win)
    down = Line(Point(300, 250), Point(300, 290))
    down.draw(win)
    i = 6
    guesses = []
    hidden_word = make_hidden_secret(secret_word, guesses)
    msg4 = Text(Point(400, 660), "")
    msg4.draw(win)
    letter_input = Entry(Point(550, 660), 1)
    while i != 0 and not won(hidden_word):
        hidden_word = make_hidden_secret(secret_word, guesses)
        msg1 = Text(Point(400, 600), "Already Guessed: {}".format(guesses))
        msg1.draw(win)
        msg2 = Text(Point(400, 620), "Guesses Remaining: {}".format(i))
        msg2.draw(win)
        msg3 = Text(Point(400, 640), "{}".format(hidden_word))
        msg3.draw(win)
        msg4.setText("Guess a Letter:")
        letter_input = Entry(Point(550, 660), 1)
        letter_input.draw(win)
        letter = letter_input.getText()
        if not already_guessed(letter, guesses) and letter_in_secret_word(letter, secret_word):
            guesses.append(letter)
        elif already_guessed(letter, guesses):
            pass
        else:
            if i == 6:
                face = Circle(Point(300, 290), 10)
                face.draw(win)
            if i == 5:
                body = Line(Point(300, 290), Point(300, 340))
                body.draw(win)
            if i == 4:
                arml = Line(Point(298, 300), Point(290, 320))
                arml.draw(win)
            if i == 3:
                armr = Line(Point(302, 300), Point(312, 320))
                armr.draw(win)
            if i == 2:
                legl = Line(Point(298, 340), Point(290, 360))
                legl.draw(win)
            if i == 1:
                legr = Line(Point(302, 340), Point(313, 360))
                legr.draw(win)
            guesses.append(letter)
            i = i - 1
    if won(hidden_word):
        letter_input.undraw()
        msg4.setText("Winner!, Click to Close Window")
        win.getMouse()
        win.close()
    else:
        letter_input.undraw()
        msg4.setText("Sorry, You Did Not Guess the Word, Click to Close Window")
        win.getMouse()
        win.close()


def play_command_line(secret_word):
    i = 6
    guesses = []
    hidden_word = make_hidden_secret(secret_word, guesses)
    while i != 0 and not won(hidden_word):
        hidden_word = make_hidden_secret(secret_word, guesses)
        print("Already Guessed:", guesses)
        print("Guesses Remaining:", i)
        print(hidden_word)
        letter = input("Guess a Letter: ")
        if not already_guessed(letter, guesses) and letter_in_secret_word(letter, secret_word):
            guesses.append(letter)
        elif already_guessed(letter, guesses):
            pass
        else:
            guesses.append(letter)
            i = i - 1
    if won(hidden_word):
        print("Winner!")
        print(secret_word)
    else:
        print("Sorry, You Did Not Guess the Word")
        print("The Word Was", secret_word)


if __name__ == '__main__':
    pass
    # list_words = get_words("words.txt")
    # secret_word = get_random_word(list_words)
    # print(secret_word)
    # play_command_line(secret_word)
    # play_graphics(secret_word)

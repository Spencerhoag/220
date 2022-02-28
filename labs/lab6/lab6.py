from graphics import *


def vigenere():
    win = GraphWin("Vigenere", 600, 600)
    win.setBackground("white")
    msg = Text(Point(50, 40), "Message to code")
    msg.draw(win)
    msg_input = Entry(Point(400, 40), 50)
    msg_input.draw(win)
    key = Text(Point(40, 70), "Enter keyword")
    key.draw(win)
    key_input = Entry(Point(400, 70), 50)
    key_input.draw(win)
    button = Rectangle(Point(280, 90), Point(320, 120))
    button.draw(win)
    button_text = Text(Point(300, 105), "Encode")
    button_text.draw(win)
    win.getMouse()
    button.undraw()
    button_text.setText("Resulting Message")
    msg_upper = msg_input.getText().upper()
    final_msg = msg_upper.strip(" ")
    key_upper = key_input.getText().upper()
    answer = ""
    for i in range(len(final_msg)):
        msg_val = ord(final_msg[i])
        key_val = ord(key_upper[i % len(key_upper)])
        msg_val = msg_val - 65
        key_val = key_val - 65
        sum_ = msg_val + key_val
        sum_ = sum_ % 26
        final = sum_ + 65
        final = chr(final)
        print(final)
        answer = answer + final
    answer_text = Text(Point(300, 120), answer)
    answer_text.draw(win)
    close_text = Text(Point(300, 570), "Click Anywhere to Close Window")
    close_text.draw(win)
    win.getMouse()
    win.close()


vigenere()
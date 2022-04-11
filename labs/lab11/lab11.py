"""
lab11.py
"""

from random import randint
from lab10.button import Button
from lab10.door import Door
from graphics import *


def main():
    win = GraphWin("Three Door Game", 600, 600)
    win.setBackground("white")
    wins_shape = Rectangle(Point(50, 40), Point(100, 100))
    loss_shape = Rectangle(Point(100, 40), Point(150, 100))
    wins_txt = Text(Point(75, 30), "Wins")
    loss_txt = Text(Point(125, 30), "Losses")
    wins_txt.draw(win)
    loss_txt.draw(win)
    wins_msg = 0
    loss_msg = 0
    wins_box = Button(wins_shape, wins_msg)
    loss_box = Button(loss_shape, loss_msg)
    wins_box.draw(win)
    loss_box.draw(win)
    play_msg = Text(Point(300, 150), "Click to guess which is the secret door!")
    play_msg.draw(win)
    button_shape = Rectangle(Point(350, 20), Point(500, 100))
    exit_msg = "Exit"
    door_shape1 = Rectangle(Point(50, 200), Point(190, 400))
    close_msg = "Door 1"
    door_shape1.setFill("red")
    button = Button(button_shape, exit_msg)
    door = Door(door_shape1, close_msg)
    button.draw(win)
    door.draw(win)
    door_shape2 = Rectangle(Point(225, 200), Point(365, 400))
    close_msg2 = "Door 2"
    door_shape2.setFill("red")
    door2 = Door(door_shape2, close_msg2)
    door2.draw(win)
    door_shape3 = Rectangle(Point(405, 200), Point(545, 400))
    close_msg3 = "Door 3"
    door_shape3.setFill("red")
    door3 = Door(door_shape3, close_msg3)
    door3.draw(win)
    playing = True
    while playing:
        doors_list = [door, door2, door3]
        ran_num = randint(0, 2)
        ran_door = doors_list[ran_num]
        ran_door.set_secret(True)
        doors_list.remove(ran_door)
        clickpoint = win.getMouse()
        if button.is_clicked(clickpoint):
            exit()
        elif ran_door.is_clicked(clickpoint):
            ran_door.color_door("green")
            play_msg.setText("Winner! -- Click Anywhere to Play Again! --")
            wins_msg = wins_msg + 1
            wins_box.set_label(wins_msg)
            play_again = win.getMouse()
            if button.is_clicked(play_again):
                exit()
            else:
                pass
        elif doors_list[0].is_clicked(clickpoint) or doors_list[1].is_clicked(clickpoint):
            ran_door.color_door("green")
            play_msg.setText("Incorrect, Sorry.  -- Click Anywhere to Play Again! --")
            loss_msg = loss_msg + 1
            loss_box.set_label(loss_msg)
            play_again2 = win.getMouse()
            if button.is_clicked(play_again2):
                exit()
            else:
                pass
        ran_door.set_secret(False)
        ran_door.color_door("red")
        play_msg.setText("Click to guess which is the secret door!")


if __name__ == '__main__':
    main()

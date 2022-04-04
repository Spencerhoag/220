"""
lab10.py
"""

from button import Button
from door import Door
from graphics import *


def main():
    win = GraphWin("Three Door Game", 600, 600)
    win.setBackground("white")
    button_shape = Rectangle(Point(100, 20), Point(500, 100))
    exit_msg = "Exit"
    door_shape = Rectangle(Point(200, 120), Point(340, 600))
    close_msg = "closed"
    door_shape.setFill("red")
    button = Button(button_shape, exit_msg)
    door = Door(door_shape, close_msg)
    button.draw(win)
    door.draw(win)
    playing = True
    while playing:
        clickpoint = win.getMouse()
        if button.is_clicked(clickpoint):
            exit()
        elif door.is_clicked(clickpoint):
            if door.get_label() == "open":
                door.close("red", "closed")
            elif door.get_label() == "closed":
                door.open("white", "open")


if __name__ == '__main__':
    main()



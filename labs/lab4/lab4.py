import time
import graphics
from graphics import *


def greeting_card():
    win = GraphWin("Heart", 800, 800)
    win.setBackground("white")
    heart = Polygon(Point(400, 650), Point(170, 160), Point(400, 250), Point(630, 160))
    heart.setFill("pink")
    heart.setOutline("black")
    message = Text(Point(400, 400), "Happy Valentine's Day!")
    close_text = Text(Point(400, 760), " ")
    arrow = Line(Point(770, 100), Point(400, 500))
    arrow.setArrow("last")
    arrow.draw(win)
    heart.draw(win)
    message.draw(win)
    close_text.draw(win)
    for i in range(100):
        arrow.move(-10, 10)
        time.sleep(0.1)
    close_text = Text(Point(400, 760), "Click anywhere to close")
    close_text.draw(win)
    win.getMouse()
    win.close()

greeting_card()
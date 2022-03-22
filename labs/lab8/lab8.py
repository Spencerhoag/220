from graphics import GraphWin, Circle, Point, color_rgb
from random import randint
import math
import time


def get_random(move_amount):
    rand_int = randint(-move_amount, move_amount)
    return rand_int


def did_collide(circle_one, circle_two):
    center1 = circle_one.getCenter()
    center2 = circle_two.getCenter()
    center1x = center1.getX()
    center1y = center1.getY()
    center2x = center2.getX()
    center2y = center2.getY()
    radius1 = circle_one.getRadius()
    radius2 = circle_two.getRadius()
    dist = math.sqrt((center2x - center1x) ** 2 + (center2y - center1y) ** 2)
    radsum = radius1 + radius2
    return dist <= radsum


def hit_vertical(circle_ball, win):
    radius = circle_ball.getRadius()
    return circle_ball.getCenter().getX() - radius <= 0 or circle_ball.getCenter().getX() + radius >= win.getWidth()


def hit_horizontal(circle_ball, win):
    radius = circle_ball.getRadius()
    return circle_ball.getCenter().getY() - radius <= 0 or circle_ball.getCenter().getY() + radius >= win.getHeight()


def get_random_color():
    ran_color = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return ran_color


def bumper():
    win = GraphWin("Bumper", 700, 700)
    win.setBackground("white")
    circle_one = Circle(Point(20, 80), 15)
    circle_one.setFill(get_random_color())
    circle_one.draw(win)
    circle_two = Circle(Point(80, 20), 15)
    circle_two.setFill(get_random_color())
    circle_two.draw(win)
    circle1x = get_random(10)
    circle1y = get_random(10)
    circle2x = get_random(10)
    circle2y = get_random(10)
    while True:
        circle_one.move(circle1x, circle1y)
        circle_two.move(circle2x, circle2y)
        if did_collide(circle_one, circle_two):
            circle1x = circle1x * -1
            circle1y = circle1y * -1
            circle2x = circle2x * -1
            circle2y = circle2y * -1
        if hit_vertical(circle_one, win):
            circle1x = circle1x * -1
        if hit_vertical(circle_two, win):
            circle2x = circle2x * -1
        if hit_horizontal(circle_one, win):
            circle1y = circle1y * -1
        if hit_horizontal(circle_two, win):
            circle2y = circle2y * -1
        time.sleep(.05)


if __name__ == '__main__':
    bumper()

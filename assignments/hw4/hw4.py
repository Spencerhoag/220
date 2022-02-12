"""
Name: <Spencer Hoag>
<Hw4>.py

Problem: <The first program creates a window that for every user click, it draws a square and clones that square every
click, then closes the window with one final click. The second and third programs take the user input of points clicked
in the window to draw a shape, the rectangle then gets its perimeter and area displayed using the difference of the two
points to find length and width, and the circle gets its radius displayed, both windows closing after the user clicks
 a final time. The final program approximates pi by looping through the user inputted amount of terms, and uses
 accumulators to keep the numerator values in the formula of the sequence constant, while the arithmetic changes the
  signs for the items in the range.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        new_shape = shape.clone()
        new_shape.move(change_x, change_y)
    click_text = Text(Point(200, 200), "Click again to close")
    click_text.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 700, 700)
    message = Text(Point(100, 100), "Click two points")
    message.draw(win)
    perimeter_text = Text(Point(350, 450), "")
    perimeter_text.draw(win)
    perimeter_ans = Text(Point(350, 460), "")
    perimeter_ans.draw(win)
    area_text = Text(Point(350, 470), "")
    area_text.draw(win)
    area_ans = Text(Point(350, 480), "")
    area_ans.draw(win)
    click_point1 = win.getMouse()
    click_point1.draw(win)
    click_point2 = win.getMouse()
    click_point2.draw(win)
    rectangle2 = Rectangle(click_point1, click_point2)
    rectangle2.setFill("green")
    rectangle2.setOutline("black")
    rectangle2.draw(win)
    perimeter_text.setText("Perimeter")
    area_text.setText("Area")
    perimeter = (click_point2.getX() - click_point1.getX())**2 + (click_point2.getY() - click_point1.getY())**2
    area = (click_point2.getX() - click_point1.getX()) * (click_point2.getY() - click_point1.getY())
    perimeter_ans.setText(perimeter)
    area_ans.setText(area)
    message.setText("Click again to close")
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 700, 700)
    message = Text(Point(100, 100), "Click a center point, then a point on the circumference")
    radius_text = Text(Point(350, 600), "")
    radius_text.draw(win)
    radius_answer = Text(Point(350, 610), "")
    radius_answer.draw(win)
    message.draw(win)
    click_1 = win.getMouse()
    click_1.draw(win)
    click_2 = win.getMouse()
    click_2.draw(win)
    x_center = click_1.getX()
    y_center = click_1.getY()
    x_radius = click_2.getX()
    y_radius = click_2.getY()
    x_square = (x_radius - x_center) * (x_radius - x_center)
    y_square = (y_radius - y_center) * (y_radius - y_center)
    radius = math.sqrt((x_square + y_square))
    shape = Circle(click_1, radius)
    shape.setFill("blue")
    shape.setOutline("black")
    shape.draw(win)
    radius_text.setText("Radius")
    radius_answer.setText(radius)
    message.setText("Click again to close")
    win.getMouse()
    win.close()


def pi2():
    num_terms = eval(input("Enter the number of terms to sum: "))
    total = 0
    num = 4
    dom = 1
    for i in range(num_terms):
        next_element = num / dom * (-1) ** i
        total = total + next_element
        dom = dom + 2
    print("pi approximation: ", total)
    print("accuracy: ", abs(math.pi - total))


if __name__ == '__main__':
    pass

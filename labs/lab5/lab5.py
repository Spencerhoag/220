from graphics import *
import math


def triangle():
    win = GraphWin("Triangle", 800, 800)
    win.setBackground("white")
    perimeter_text = Text(Point(400, 700), " ")
    perimeter_text.draw(win)
    perimeter_ans = Text(Point(400, 710), " ")
    perimeter_ans.draw(win)
    area_text = Text(Point(400, 720), " ")
    area_text.draw(win)
    area_ans = Text(Point(400, 730), " ")
    area_ans.draw(win)
    click1 = win.getMouse()
    click1.draw(win)
    click2 = win.getMouse()
    click2.draw(win)
    click3 = win.getMouse()
    click3.draw(win)
    shape = Polygon(click1, click2, click3)
    shape.setFill("blue")
    shape.setOutline("black")
    shape.draw(win)
    perimeter_text.setText("Perimeter: ")
    area_text.setText("Area: ")
    x1 = click1.getX()
    y1 = click1.getY()
    x2 = click2.getX()
    y2 = click2.getY()
    x3 = click3.getX()
    y3 = click3.getY()
    side_a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side_b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    side_c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    perimeter = side_a + side_b + side_c
    perimeter_ans.setText(perimeter)
    surf = (side_a + side_b + side_c) / 2
    area = math.sqrt(surf * (surf - side_a) * (surf - side_b) * (surf - side_c))
    area_ans.setText(area)
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_box = Entry(Point(190, 240), 3)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_box = Entry(Point(190, 270), 3)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_box = Entry(Point(190, 300), 3)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)
    shape.setFill(color_rgb(red_box.getText(), green_box.getText(), blue_box.getText()))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    sent = input("Enter a string: ")
    first = sent[0]
    print(first)
    last = sent[-1]
    print(last)
    two_5 = sent[1:6]
    print(two_5)
    concat = first + last
    print(concat)
    first3 = sent[0:3]
    for i in range(10):
        print(first3, end="")
    print()
    for j in sent:
        print(j)
    print(len(sent))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print(values[1] + values[3])
    print(values[0] + values[2])
    hi = values[1]
    for i in range(5):
        print(hi, end="")
    print()
    print(values[2:5])
    five = values[2:4]
    five.append(int("5"))
    print(five)
    all3 = []
    first = values[2]
    second = values[0]
    third = values[5]
    all3.append(first)
    all3.append(second)
    all3.append(float(third))
    print(all3)
    sum3 = []
    acc = values[2]
    acc2 = values[0]
    acc3 = values[5]
    sum3.append(acc + acc2 + float(acc3))
    for j in sum3:
        print(float(j))
    print(len(values))


def another_series():
    print("Enter the number of terms: ")
    terms = eval(input(" "))
    sums = 0
    for i in range(0, terms)[2:7:2]:
        sums = sums + i
    print(sums)


def target():
    win = GraphWin("Target", 800, 800)
    win.setBackground("grey")
    yellow = Circle(Point(400, 400), 220)
    yellow.setFill("yellow")
    red = Circle(Point(400, 400), 270)
    red.setFill("red")
    blue = Circle(Point(400, 400), 310)
    blue.setFill("blue")
    black = Circle(Point(400, 400), 350)
    black.setFill("black")
    white = Circle(Point(400, 400), 390)
    white.setFill("white")
    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)
    msg = Text(Point(400, 780), "Click to close")
    msg.draw(win)
    win.getMouse()
    win.close()
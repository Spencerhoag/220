from graphics import Circle, Line, Polygon, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        self.mouth.undraw()
        triangle = Polygon(Point(160, 250), Point(240, 250), Point(200, 290))
        triangle.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        circle = Circle(Point(200, 260), 15)
        circle.draw(self.window)

    def wink(self):
        self.smile()
        self.left_eye.undraw()
        eye_wink = Line(Point(100, 100), Point(150, 100))
        eye_wink.draw(self.window)


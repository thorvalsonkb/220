"""
Name: <Kelsey Thorvalson>
<hw4>.py

Problem: <Creates interactive windows and approximates pi with user input>

Certification of Authenticity:
<I certify that this assignment is entirely my own work>
"""

import math
from graphics import GraphWin, Point, Rectangle, Circle, Text


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(100, 300), Point(150, 350))
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
        new_shape.draw(win)

    click_text = Text(Point(200, 200), "Click again to close")
    click_text.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    first = win.getMouse()
    first.draw(win)
    second = win.getMouse()
    second.draw(win)
    rec = Rectangle(first, second)
    rec.setFill('red')
    rec.draw(win)

    p1_x = first.getX()
    p1_y = first.getY()
    p2_x = second.getX()
    p2_y = second.getY()

    bot = abs(p1_x - p2_x)
    side = abs(p1_y - p2_y)
    area = bot * side
    perimeter = (bot * 2) + (side * 2)

    area_text = Text(Point(250, 370), area)
    perimeter_text = Text(Point(250, 400), perimeter)
    area_text.draw(win)
    perimeter_text.draw(win)

    click_text = Text(Point(250, 450), "Click anywhere to close")
    click_text.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 500, 500)
    center = win.getMouse()
    center.draw(win)
    circum = win.getMouse()
    circum.draw(win)

    center_x = center.getX()
    center_y = center.getY()
    p2_x = circum.getX()
    p2_y = circum.getY()
    radius = math.sqrt((p2_x - center_x) ** 2 + (p2_y - center_y) ** 2)

    shape = Circle(center, radius)
    shape.setFill('blue')
    shape.draw(win)
    rad_text = Text(Point(250, 400), radius)
    rad_text.draw(win)

    click_text = Text(Point(250, 450), "Click anywhere to close")
    click_text.draw(win)
    win.getMouse()
    win.close()


def pi2():
    terms = int(input("enter the number of terms to sum"))
    val_pi = 0
    for i in range(terms):
        approx = ((-1) ** i) / (2 * i + 1)
        val_pi = val_pi + approx
    accuracy = math.pi - (val_pi * 4)
    print("pi approximation: ", val_pi * 4)
    print("accuracy: ", accuracy)


if __name__ == '__main__':
    pass

"""
Kelsey Thorvalson
lab5.py
This program creates graphwins with user interaction as well
as list and string processes.
I certify that this assignment is entirely my own work.
"""

import math
from graphics import GraphWin, Polygon, Entry, Text, Point, Circle, color_rgb


def triange():
    win = GraphWin("Triangle", 600, 600)
    win.setCoords(0, 0, 10, 10)

    first = win.getMouse()
    first.draw(win)
    second = win.getMouse()
    second.draw(win)
    third = win.getMouse()
    third.draw(win)
    triangle = Polygon(first, second, third)
    triangle.setFill('red')
    triangle.draw(win)

    p1_x = first.getX()
    p1_y = first.getY()
    p2_x = second.getX()
    p2_y = second.getY()
    p3_x = third.getX()
    p3_y = third.getY()

    linea_x = abs(p2_x - p1_x)
    linea_y = abs(p2_y - p1_y)
    lineb_x = abs(p3_x - p2_x)
    lineb_y = abs(p3_y - p2_y)
    linec_x = abs(p1_x - p3_x)
    linec_y = abs(p1_y - p3_y)

    line_a = math.sqrt(linea_x ** 2 + linea_y ** 2)
    line_b = math.sqrt(lineb_x ** 2 + lineb_y ** 2)
    line_c = math.sqrt(linec_x ** 2 + linec_y ** 2)
    perimeter = line_a + line_b + line_c
    var_s = (line_a + line_b + line_c) / 2
    area = math.sqrt(var_s * (var_s - line_a) * (var_s - line_b) * (var_s - line_c))

    perimeter_text = Text(Point(5, 2), "Perimeter: " + str(perimeter))
    area_text = Text(Point(5, 1), "Area: " + str(area))
    perimeter_text.draw(win)
    area_text.draw(win)

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
    red_entry_pt = Point(win_width / 2 + 23, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(red_entry_pt, 10)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_entry_pt = red_entry_pt.clone()
    green_entry_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(green_entry_pt, 10)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_entry_pt = red_entry_pt.clone()
    blue_entry_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(blue_entry_pt, 10)

    # display rgb text
    red_text.draw(win)
    red_entry.draw(win)
    green_text.draw(win)
    green_entry.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)

    # get colors
    for i in range(5):
        win.getMouse()
        redAmt = eval(red_entry.getText())
        greenAmt = eval(green_entry.getText())
        blueAmt = eval(blue_entry.getText())
        shape.setFill(color_rgb(redAmt, greenAmt, blueAmt))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_string = input("Enter a word or sentence: ")
    first_letter = user_string[0]
    last_letter = user_string[-1]
    print(first_letter)
    print(last_letter)
    characters = user_string[1:5]
    print(characters)
    conc = (first_letter + last_letter)
    print(conc)
    first_three = user_string[0:4]
    three_ten = first_three * 10
    print(three_ten)
    length = len(user_string)
    for i in range(length):
        print(user_string[i])
    print(length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = (values[1] + values[3])
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    order = [2, 3, 0]
    x = [values[i] for i in order]
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Enter number of terms: "))
    for i in range(3):
        var = i * 2 + 2
        print(var[i % terms])


def target():
    width = 500
    height = 500
    win = GraphWin("Target", width, height)
    radius = width / 2
    shape = Circle(Point(250, 250), radius)
    shape.draw(win)
    radius_dif = radius / 5
    center = shape.getCenter()
    black = Circle(center, radius - radius_dif)
    black.setFill('black')
    blue = Circle(center, radius - (radius_dif * 2))
    blue.setFill('blue')
    red = Circle(center, radius - (radius_dif * 3))
    red.setFill('red')
    yellow = Circle(center, radius - (radius_dif * 4))
    yellow.setFill('yellow')
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)

    close_text = Text(Point(250, 250), "Click to Close")
    close_text.draw(win)

    win.getMouse()
    win.close()

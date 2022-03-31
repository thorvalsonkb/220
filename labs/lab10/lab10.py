"""
Kelsey Thorvalson
lab10.py
this program creates a window to open and close a door with classes
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Rectangle, Point
from Button import Button
from Door import Door


def main():
    win = GraphWin('Test', 500, 500)

    # door
    door_shape = Rectangle(Point(165, 480), Point(335, 120))
    d = Door(door_shape, 'Closed')
    d.color_door('white')
    d.draw(win)

    # button
    button_shape = Rectangle(Point(165, 20), Point(335, 100))
    b = Button(button_shape, 'Exit')
    b.draw(win)
    b.color_button('gray')

    # door change
    while d.is_clicked(win.getMouse()) is True:
        d.color_door('red')
        d.set_label('Open')
        d.is_clicked(win.getMouse())
        d.color_door('white')
        d.set_label('Closed')

    b.is_clicked(win.getMouse())
    win.close()

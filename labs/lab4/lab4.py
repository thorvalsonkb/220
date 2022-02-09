from graphics import Point, GraphWin, Text, Polygon, Circle, Line
from time import sleep

def greeting_card():
    win = GraphWin("Greeting Card", 700, 700)
    win.setCoords(0, 0, 10, 10)
    win.setBackground('pink')
    message = Text(Point(5, 1.5), "Happy Valentine's Day!")
    message.setSize(22)
    message.setStyle("bold")
    message.setFill('red')
    message.draw(win)

    heart_1 = Circle(Point(4, 7), 1.5)
    heart_1.setFill('red')
    heart_1.setOutline('red')
    heart_1.draw(win)

    heart_bottom = Polygon(Point(2.58, 6.5), Point(7.42, 6.5), Point(5, 2.75))
    heart_bottom.setFill('red')
    heart_bottom.setOutline('red')
    heart_bottom.draw(win)

    arrow = Line(Point(2.5, 2.5), Point(3.5, 3.5))
    arrow.setArrow("last")
    arrow.setWidth(7)
    arrow.draw(win)

    heart_2 = Circle(Point(6, 7), 1.5)
    heart_2.setFill('red')
    heart_2.setOutline('red')
    heart_2.draw(win)

    for i in range(8):
        arrow.move(1, 1)
        sleep(.25)

    click_text = Text(Point(5, 0.75), "Click anywhere to close")
    click_text.draw(win)
    win.getMouse()


greeting_card()

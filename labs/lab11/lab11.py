"""
Kelsey Thorvalson
lab11.py
This program
I certify that this is entirely own work
"""

from graphics import GraphWin, Rectangle, Point, Text
from random import randint
from lab10.Button import Button
from lab10.Door import Door


def three_door_game():
    win = GraphWin('Three Door Game', 500, 600)
    win.setBackground('gray')
    # button
    button_shape = Rectangle(Point(350, 30), Point(460, 90))
    button = Button(button_shape, 'Exit')
    button.color_button('white')
    button.draw(win)
    # doors
    door_y1 = 150
    door_y2 = 500
    door_one_shape = Rectangle(Point(40, door_y1), Point(150, door_y2))
    door_one = Door(door_one_shape, 'Door 1')
    door_one.color_door('brown')
    door_one.draw(win)
    door_two_shape = Rectangle(Point(190, door_y1), Point(300, door_y2))
    door_two = Door(door_two_shape, 'Door 2')
    door_two.color_door('brown')
    door_two.draw(win)
    door_three_shape = Rectangle(Point(340, door_y1), Point(450, door_y2))
    door_three = Door(door_three_shape, 'Door 3')
    door_three.color_door('brown')
    door_three.draw(win)
    # text
    win_text = Text(Point(65, 20), 'wins')
    lose_text = Text(Point(122, 20), 'losses')
    win_text.draw(win)
    lose_text.draw(win)
    win_shape = Rectangle(Point(40, 30), Point(95, 90))
    win_shape.setFill('gray')
    win_shape.draw(win)
    lose_shape = win_shape.clone()
    lose_shape.move(55, 0)
    lose_shape.draw(win)
    win_count = Text(win_shape.getCenter(), 0)
    lose_count = Text(lose_shape.getCenter(), 0)
    win_count.draw(win)
    lose_count.draw(win)
    top_text = Text(Point(250, 125), 'I have a secret door!')
    bottom_text = Text(Point(250, 550), 'Click to guess which is the secret door!')
    top_text.draw(win)
    bottom_text.draw(win)
    # secret
    doors = [door_one, door_two, door_three]
    click = win.getMouse()
    while not button.is_clicked(click):
        rand_num = randint(0, 2)
        doors[rand_num].set_secret(True)
        click = win.getMouse()
        for door in doors:
            if door.is_clicked(click):
                if door.is_secret():
                    door.color_door('green')
                    top_text.setText('You win!')
                    bottom_text.setText('click anywhere to play again')
                    win_count.setText(int(win_count.getText()) + 1)
                else:
                    door.color_door('red')
                    top_text.setText('Sorry, incorrect.')
                    bottom_text.setText('click anywhere to play again')
                    lose_count.setText(int(lose_count.getText() + 1))
                    for win_door in doors:
                        if win_door.is_secret():
                            win_door.color_door('green')
                win.getMouse()
        doors[rand_num].set_secret(False)
        door_one.color_door('brown')
        door_two.color_door('brown')
        door_three.color_door('brown')
        top_text.setText('I have a secret door!')
        bottom_text.setText('Click to guess which is the secret door!')
    win.close()

"""
Kelsey Thorvalson
lab6.py
This program creates graphwins with user input to create an encrypted message.
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Entry, Text, Point, Rectangle


def vigenere():
    win = GraphWin("Vigenere", 600, 450)
    win.setCoords(0, 0, 10, 10)

    message_text = Text(Point(2.5, 9), "Message to code: ")
    message_text.draw(win)
    keyword_text = Text(Point(2.5, 8), "Enter keyword: ")
    keyword_text.draw(win)

    button = Rectangle(Point(4, 7), Point(6, 6))
    button.draw(win)
    button_center = button.getCenter()
    text_encode = Text(button_center, "Encode")
    text_encode.draw(win)

    entry_mes = Entry(Point(6, 9), 20)
    entry_key = Entry(Point(6, 8), 20)
    entry_mes.draw(win)
    entry_key.draw(win)
    win.getMouse()
    message = entry_mes.getText()
    keyword = entry_key.getText()
    better_message = message.upper().replace(" ", "")
    better_key = keyword.upper().replace(" ", "")
    message_length = len(better_message)
    keyword_length = len(better_key)

    button.undraw()
    text_encode.undraw()

    final = ""
    for i in range(message_length):
        old_mes = ord(better_message[i])
        key = ord(better_key[i % keyword_length])
        our_mes = old_mes - 65
        our_key = key - 65
        new_mes = (our_mes + our_key) % 26
        new_mes_range = new_mes + 65
        mes = chr(new_mes_range)
        final = final + mes

    result_text = Text(Point(5, 4.5), "Resulting Message")
    result_text.draw(win)
    answer_text = Text(Point(5, 4), final)
    answer_text.draw(win)

    click_text = Text(Point(5, 0.75), "Click anywhere to close")
    click_text.draw(win)
    win.getMouse()
    win.close()


vigenere()

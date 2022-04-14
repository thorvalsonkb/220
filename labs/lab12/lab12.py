"""
Kelsey Thorvalson
lab12.py
This assignment is to practice different ways to use while loops
I certify that this is assignment is entirely my own work.
"""

from random import randint


def find_and_remove(list, value):
    value_index = list.index(value)
    list[value_index] = 'Kelsey'
    print(list)


def good_input():
    user_in = eval(input('Enter a number between 1 and 10:'))
    if 1 <= user_in <= 10:
        return user_in
    while user_in < 1 or user_in > 10:
        if user_in < 1:
            print('Your input was too low.')
            user_in = eval(input('Enter a number between 1 and 10'))
        elif user_in > 10:
            print('Your input was too high.')
            user_in = eval(input('Enter a number between 1 and 10'))


def num_digits():
    digits = 0
    user_in = eval(input('Enter a positive number (enter 0 or a negative number to exit):'))
    while user_in > 0:
        while user_in > 0:
            digits = digits + 1
            user_in = user_in // 10
        print('There are', digits, 'digits')
        digits = 0
        user_in = eval(input('Enter a positive number (enter 0 or a negative number to exit):'))


def hi_lo_game():
    guesses = 0
    rand = randint(1, 100)
    print(rand)
    while guesses < 7:
        guesses = guesses + 1
        user_in = eval(input('Enter a number from 1 to 100:'))
        if user_in > rand:
            print('too high')
        elif user_in < rand:
            print('too low')
        else:
            print('You win in', guesses, 'guesses')
            return rand
    print('Sorry, you lose. The number was', rand)


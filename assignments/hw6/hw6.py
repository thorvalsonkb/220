"""
Name: <Kelsey Thorvalson>
<hw6>.py

Problem: <>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

import math

def cash_converter():
    user_int = eval(input("enter an integer: "))
    answer = "That is ${price:.2f}"
    print(answer.format(price=user_int))


def encode():
    message = input("enter a message: ")
    key = int(input("enter a key: "))
    message_length = len(message)
    final = ""
    for i in range(message_length):
        old_mes = ord(message[i])
        new_mes = old_mes + key
        mes = chr(new_mes)
        final = final + mes
    print(final)


def sphere_area(radius: float):
    surface = 4 * math.pi * math.pow(radius, 2)
    return surface


rad = float(input("what is the radius"))
x = sphere_area(rad)
print(x)


def sphere_volume(radius: float):
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    return volume


rad_two = float(input("radius:"))
y = sphere_volume(rad_two)
print(y)


def sum_n(number):
    pass


def sum_n_cubes(number):
    pass


def encode_better():
    message = input("enter a message: ")
    keyword = input("enter a key word: ")
    message_length = len(message)
    key_length = len(keyword)
    final = ""
    for i in range(message_length):
        old_mes = ord(message[i])
        key = ord(keyword[i % key_length])
        our_mes = old_mes - 65
        our_key = key - 65
        new_mes = (our_mes + our_key) % 58
        new_mes_range = new_mes + 65
        mes = chr(new_mes_range)
        final = final + mes
    print(final)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

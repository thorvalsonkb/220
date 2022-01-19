"""
Name: <Kelsey Thorvalson>
<hw1>.py

Problem: <This program solves simple evaluation problems with user input>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    area = length * width * height
    print("Area =", area)


def shooting_percentage():
    total = eval(input("Enter the player's total shots:"))
    made = eval(input("Enter how many shots the player made:"))
    percent = made/total * 100
    print("Shooting Percentage:", percent, "%")


def coffee():
    pounds = eval(input("How many pounds of coffee would you like?"))
    total = pounds * 10.5 + pounds * 0.86 + 1.5
    print("Your total is:", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers/1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass

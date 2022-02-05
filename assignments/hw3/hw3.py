"""
Name: <Kelsey Thorvalson>
<hw3>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    grades = int(input("How many grades will you enter?"))
    total = 0
    for i in range(1, grades + 1):
        enter = int(input("Enter grade: "))
        total = total + enter
    ave = total / grades
    print(ave)


def tip_jar():
    total = 0
    for i in range(1, 6):
        tip = eval(input("How mush would you like to donate?"))
        total = total + tip
    print("total tips: ", total)


def newton():
    user_x = eval(input("What number do you want to square root?"))
    approx = int(input("How many times should we improve the approximation?"))
    for i in range (1, approx + 1):
        approx = (approx + (approx / approx)) / 2
    print("the square root is approximately", user_x)


def sequence():
    terms = int(input("how many terms would you like?"))
    for i in range(1, terms + 1, 2):
        for j in range(1):
            print(i)
        print(i)


def pi():
    pass


if __name__ == '__main__':
    pass

"""
Name: <Kelsey Thorvalson>
<hw2>.py

Problem: <Simple Python programs that do input, produce output and do arithmetic>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""
import math


def sum_of_threes():
    upper = eval(input("what is the upper bound?"))
    val = 0
    for i in range(0, upper + 1, 3):
        val = val + i
    print("sum of threes is", val)




def multiplication_table():
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print(i * j, end="\t")
        print()


def triangle_area():
    sidea = eval(input("Enter side a length:"))
    sideb = eval(input("Enter side b length:"))
    sidec = eval(input("Enter side c length:"))
    var_s = (sidea + sideb + sidec) / 2
    area = math.sqrt(var_s * (var_s - sidea) * (var_s - sideb) * (var_s - sidec))
    print("area is", area)


def sum_squares():
    lower = int(input("Enter lower range:"))
    upper = int(input("Enter upper range:"))
    final = 0
    for i in range(lower, upper + 1):
        var = i * i
        final = final + var
    print(final)


def power():
    base = eval(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    final = 1
    for i in range(1, exponent + 1):
        final = final * base
    print(base, "^", exponent, "=", final)


if __name__ == '__main__':
    pass

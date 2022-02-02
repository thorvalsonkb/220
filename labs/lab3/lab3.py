"""
Kelsey Thorvalson
lab3.py
This program is used to calculate average number of cars on roads for different days.
I certify that this assignment is entirely my own work.
"""
def traffic():
    roads = int(input("How many roads were surveyed?"))
    total_cars = 0
    total_roads = 0
    for i in range(1, roads + 1):
        ave = 0
        print("How many days was road", i, "surveyed?")
        days = eval(input(""))
        for j in range(1, days + 1):
            print("How many cars traveled on day", j, "?")
            cars = eval(input(""))
            ave = ave + cars
            total_cars = total_cars + cars
        print("Road", i, "average vehicles per day:", ave / days)
    print("Total number of vehicles traveled on all roads: ", total_cars)
    ave_road = total_cars / roads
    print("Average number of vehicles per road: ", round(ave_road, 2))

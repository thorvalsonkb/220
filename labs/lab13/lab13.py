"""
Kelsey Thorvalson
lab13.py
This program takes a set of trades per second from a day and alerts if they are at/pass a certain threshold
I certify that this assignment is entirely my own work.
"""


def trade_alert(filename):
    file = open(filename, 'r')
    line = file.readline()
    line_list = line.split(' ')
    for i in range(len(line_list)):
        seconds = 1
        if int(line_list[i]) > 830:
            seconds = seconds + i
            print('Warning: Trading volume exceeded 830 at', seconds, 'seconds.')
        if int(line_list[i]) == 500:
            seconds = seconds + i
            print('Alert: Trading volume at 500 at', seconds, 'seconds.')
    file.close()

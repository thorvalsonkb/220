"""
Kelsey Thorvalson
lab7.py
This program takes a file consisting of numerica data and outputs new data using information from the file
I certify that this assignment is entirely my own work
"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    in_file_strings = in_file.readlines()
    string_count = len(in_file_strings)
    class_ave = 0
    for i in range(string_count):
        string_index = in_file_strings[i]
        colon = string_index.find(":")
        first_half = string_index[:colon]
        second_half = string_index[colon + 2:]
        second_list = second_half.split()
        second_length = len(second_list)
        denominator = second_length / 2
        total_weight = 0
        total_grade = 0
        class_ave = 0
        for j in range(0, second_length, 2):
            weight = eval(second_list[j])
            grade = eval(second_list[j + 1])
            total_weight = total_weight + weight
            total_grade = total_grade + grade
            class_ave = class_ave + (weight * grade)
        if total_weight == 100:
            print(first_half + "'s average:", round((total_grade / denominator), 1))
        elif total_weight < 100:
            print(first_half + "'s average: Error: The weights are less than 100.")
        else:
            print(first_half + "'s average: Error: The weights are more than 100.")
    print("Class average:", class_ave / 100)
    out_file.close()
    in_file.close()


weighted_average('grades.txt', 'avg.txt')

from graphics import Rectangle, Point


def read_data(filename):
    in_file = open(filename, 'r')
    file_list = in_file.readlines()
    in_file.close()
    return file_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        return False


def selection_sort(values):
    left_index = 0
    while left_index <= len(values) - 1:
        minimum = values[left_index]
        min_index = left_index
        for i in range(left_index, len(values)):
            if minimum > values[i]:
                minimum = values[i]
                min_index = i
        values[left_index], values[min_index] = minimum, values[left_index]
        left_index = left_index + 1


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    width = abs(x1 - x2)
    length = abs(y1 - y2)
    area = width * length
    return area


def rect_sort(rectangles):
    left_index = 0
    while left_index <= len(rectangles) - 1:
        minimum = calc_area(rectangles[left_index])
        min_index = left_index
        for i in range(left_index, len(rectangles)):
            if minimum > calc_area(rectangles[i]):
                minimum = rectangles[i]
                min_index = i
        rectangles[left_index], rectangles[min_index] = minimum, rectangles[left_index]
        left_index = left_index + 1

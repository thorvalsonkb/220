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


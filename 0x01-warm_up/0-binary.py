#!/usr/bin/python3
''' use binary search algorith to find a value'''

def binary_search(array, value):
    ''' find a value using binary search algorithm'''


    mid_point = int(len(array) / 2)
    print(mid_point)
    if array[mid_point] == value:
         return mid_point
    if len(array) == 1:
        return -1
    elif value < array[mid_point]:
        print ("going through lower array")
        index = binary_search(array[:mid_point - 1], value)
        return index
    else:
        index = binary_search(array[mid_point:], value)
        return index


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = -1
    index = binary_search(array, value)
    print ("found value at index---> {}".format(index))

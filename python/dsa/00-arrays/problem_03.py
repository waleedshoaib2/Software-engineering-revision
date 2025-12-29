def minimum_number(array):
    min_value = array[0]

    for x in array:
        if min_value > x:
            min_value = x
    return min_value

array = [8, 6, 4, 10, 2]

print(minimum_number(array))
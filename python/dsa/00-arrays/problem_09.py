def linear_search(number, array):
    for i in range(len(array)):
        if array[i] == number:
            return i
    else:
        return -1

array = [4, 2, 7, 1, 9]
number = 7


print(linear_search(number, array))

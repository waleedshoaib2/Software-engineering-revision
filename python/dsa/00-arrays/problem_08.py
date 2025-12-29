def check_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

array = [1, 3, 5, 6, 9, 7]
print(check_sorted(array))    
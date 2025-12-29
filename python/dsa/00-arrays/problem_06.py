def odd_number(array):
    total = 0
    for x in array:
        if x%2 != 0:
            total += 1

    return total

array = [33,42,42,12,11,33,13,9]
print(odd_number(array))
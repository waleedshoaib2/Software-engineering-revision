def even_num(array):
    total = 0
    for x in array:
        if x%2==0:
            total +=1
    return total

array = [33,44,32,45,23,21,20]
print(even_num(array))
def count_number(number, array):
    count = 0
    for x in range(len(array)):
        if array[x] == number:
            count +=1
    return count


array = [1,2 ,3 ,2 ,2 ,4]
number = 2


print(count_number(number,array))
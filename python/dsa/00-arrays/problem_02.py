# def maximum_number(array):
#     highest = 0
#     for x in array:
#         if x>highest:
#             highest = x
    
#     return highest

# array = [33,42,545,434,66,323,88]

# print(maximum_number(array))

# Above one works but what if the input is negative? We are initializing with 0, so 0 is not in the array
# better solution

def maximum_number(array):
    max_value = array[0]

    for x in array:
        if x > max_value:
            max_value = x
    return max_value
array = [-33,-42,-545,-434,-66,-323,-88]

print(maximum_number(array))
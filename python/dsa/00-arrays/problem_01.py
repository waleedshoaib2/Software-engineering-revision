def reverse_array(array):
    array.reverse()
    return array


print("Please Enter the number of integers:")
number = int(input())
print("Enter the values now: ")
array = list(map(int, input().split()))

if len(array) != number:
    print("Invalid Input")
else:
    print(reverse_array(array))

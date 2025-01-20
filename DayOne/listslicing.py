# List slicing examples

# Create a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slice the list to get the first 5 elements
first_five = my_list[:5]
print("First five elements:", first_five)

# Slice the list to get elements from index 5 to the end
from_five_onwards = my_list[5:]
print("Elements from index 5 onwards:", from_five_onwards)

# Slice the list to get elements from index 2 to 5
middle_slice = my_list[2:6]
print("Elements from index 2 to 5:", middle_slice)

# Slice the list to get every second element
every_second = my_list[::2]
print("Every second element:", every_second)

# Slice the list to get elements in reverse order
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)
# Slice the list to get every second element in reverse order
every_second_reversed = my_list[::-2]
print("Every second element in reverse order:", every_second_reversed)

# Slice the list to get elements from index 8 to 2 in reverse order
reverse_partial = my_list[8:1:-1]
print("Elements from index 8 to 2 in reverse order:", reverse_partial)
# Create a list with some elements
my_list = [10, 20, 30, 40, 50]

# Access elements using index
first_element = my_list[0]
second_element = my_list[1]
third_element = my_list[2]

# Print the accessed elements
print("First element:", first_element)
print("Second element:", second_element)
print("Third element:", third_element)

for x in my_list:
    print(f"{x}")

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

    # Demonstrate mutability by modifying elements
my_list[0] = 100
my_list[1] = 200
my_list[2] = 300

    # Print the modified list
print("Modified list:", my_list)
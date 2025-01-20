# Example 1: Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

# Example 2: Create a list of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Example 3: Create a list of tuples (number, square)
number_square_tuples = [(x, x**2) for x in range(10)]
print(number_square_tuples)



# Example 5: Create a list of uppercase characters
uppercase_chars = [char.upper() for char in 'hello']
print(uppercase_chars)
# Example 6: Create a list of squares with custom elements
custom_elements = [1, 3, 5, 7]
custom_squares = [x**2 for x in custom_elements]
print(custom_squares)

# Example 7: Create a list of even numbers with custom elements
custom_elements = [10, 15, 20, 25, 30]
custom_evens = [x for x in custom_elements if x % 2 == 0]
print(custom_evens)

# Example 8: Create a list of tuples (number, square) with custom elements
custom_elements = [2, 4, 6, 8]
custom_number_square_tuples = [(x, x**2) for x in custom_elements]
print(custom_number_square_tuples)

# Example 9: Flatten a list of custom lists
custom_list_of_lists = [[10, 20], [30, 40], [50, 60]]
custom_flattened = [item for sublist in custom_list_of_lists for item in sublist]
print(custom_flattened)

# Example 10: Create a list of uppercase characters with custom string
custom_string = 'world'
custom_uppercase_chars = [char.upper() for char in custom_string]
print(custom_uppercase_chars)
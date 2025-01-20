# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[1:3])  # Output: (2, 3)

# Tuples are immutable, so you cannot change their values
# my_tuple[0] = 10  # This will raise a TypeError

# You can concatenate tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# You can also use tuples in functions
def print_tuple(t):
    for item in t:
        print(item)

print_tuple(my_tuple)
# Demonstrating immutability
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'tuple' object does not support item assignment
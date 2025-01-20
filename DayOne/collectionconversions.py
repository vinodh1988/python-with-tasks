# List to Tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(f"List to Tuple: {my_tuple}")

# Tuple to List
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print(f"Tuple to List: {my_list}")

# List to Set
my_list = [1, 2, 3, 4, 4]
my_set = set(my_list)
print(f"List to Set: {my_set}")

# Set to List
my_set = {1, 2, 3, 4}
my_list = list(my_set)
print(f"Set to List: {my_list}")

# Tuple to Set
my_tuple = (1, 2, 3, 4, 4)
my_set = set(my_tuple)
print(f"Tuple to Set: {my_set}")

# Set to Tuple
my_set = {1, 2, 3, 4}
my_tuple = tuple(my_set)
print(f"Set to Tuple: {my_tuple}")

# List to Dictionary (with index as key)
my_list = ['a', 'b', 'c', 'd']
my_dict = {i: my_list[i] for i in range(len(my_list))}
print(f"List to Dictionary: {my_dict}")

# Dictionary to List (keys and values)
my_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
print(f"Dictionary to List (keys): {keys_list}")
print(f"Dictionary to List (values): {values_list}")
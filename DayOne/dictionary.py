# dictionary.py

# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: John
print(person.get("age"))  # Output: 30

# Adding a new key-value pair
person["email"] = "john@example.com"

# Updating an existing value
person["age"] = 31

# Removing a key-value pair
del person["city"]

# Iterating through keys
for key in person:
    print(key, person[key])

# Iterating through values
for value in person.values():
    print(value)

# Iterating through key-value pairs
for key, value in person.items():
    print(key, value)

# Checking if a key exists
if "name" in person:
    print("Name is present")

# Dictionary length
print(len(person))  # Output: 3

# Clearing the dictionary
person.clear()
print(person)  # Output: {}
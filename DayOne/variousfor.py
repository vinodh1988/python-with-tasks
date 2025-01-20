# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a string
for letter in "banana":
    print(letter)

# Loop through a range of numbers
for i in range(5):
    print(i)

# Loop through a range of numbers with a step
for i in range(0,10,2):
    print(i)
# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop with else
for i in range(5):
    print(i)
else:
    print("Loop is done")

# Loop through a list with index
for index, value in enumerate(fruits):
    print(index, value)
    
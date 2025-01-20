def sum_all(*args):
    print(args)
    for x in args:
        print(x)
    return sum(args)

def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(10, 20, 30))  # Output: 60
print_all(name="Alice", age=30, city="Wonderland")
print_all(a=50,b=60,c=70)
# Output:
# name: Alice
# age: 30
# city: Wonderland
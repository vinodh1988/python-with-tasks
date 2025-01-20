def greet(name="Guest"):
    return f"Hello, {name}!"

def add(a=0, b=0):
    return a + b

def multiply(x=1, y=1):
    return x * y


print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!
print(add())  # Output: 0
print(add(5, 3))  # Output: 8
print(add(a=5, b=3))  # Output: 8
print(add(b=10))  # Output: 10
print(multiply())  # Output: 1
print(multiply(y=4, x=5))  # Output: 20
def greet(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
xyz = greet
abc = greet

# Using the variable to call the function
print(xyz("Alice"))
print(abc("Bob"))

def sum(a,b):
    return a + b

add=sum
print(add(5,3))

def process(thisfun): # callback function as pareameter
    print("This is process function")
    thisfun("Data from process")
    print("End of process function")	

def display(data):
    print("This is display function")
    print(f"Data received: {data}")
    print("End of display function")

def verify(data):
    print("This is verify function")
    print(f"Data received: {data}")
    print("End of verify function")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
process(display) # six lines"
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
process(verify)
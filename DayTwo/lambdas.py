greet=lambda name: f"Hello, {name}!"
add=lambda a,b: a+b
multiply=lambda x,y: x*y
is_even=lambda x: x%2==0
is5digit=lambda x: len(str(x))==5

print(greet("Alice"))
print(add(5,3))
print(multiply(5,3))
print(is_even(10))
print(is5digit(12345))
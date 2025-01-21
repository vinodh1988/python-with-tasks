class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

    def __repr__(self):
        return f'Person({self.name}, {self.age})'
    

    
person1=Person('Alice', 25)
person2=Person('Bob', 30)
person3=Person('Charlie', 35)

person1.say_hello()
person2.say_hello()
person3.say_hello()

print(person1)
print(person2)
print(person3)
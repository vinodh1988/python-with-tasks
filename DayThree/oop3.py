class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")	

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Woof"
    def speak(self):
        Animal.speak(self)
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Meow"
    def speak(self):
        Animal.speak(self)
        return f"{self.name} says Meow!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
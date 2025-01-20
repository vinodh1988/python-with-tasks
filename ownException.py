class AgeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
    
    def __str__(self):
        return self.message
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
try:
    if age < 0 or age > 120:
        raise AgeException("Age must be between 0 and 120.")
except AgeException as e:
    print(f"AgeException: {e}")
except Exception as e:
    print(f"Exception: {e}")

    print("All Good")
    print(f"Name: {name}, Age: {age}, City: {city}")



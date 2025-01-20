data = []

for _ in range(2):
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    data.append({"name": name, "age": age, "city": city})

with open('data.txt', 'a') as file:
    for entry in data:
        file.write(f"Name: {entry['name']}, Age: {entry['age']}, City: {entry['city']}\n")


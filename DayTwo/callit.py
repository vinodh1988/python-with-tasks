import random
import json

random_number = random.randint(1, 1000)
print(random_number)

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data)
print(json_data)

with open('source.json', 'r') as file:
    source_data = json.load(file)

print(source_data)
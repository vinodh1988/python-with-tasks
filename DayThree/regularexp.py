import re

data = [
    "John Doe", "john.doe@example.com", "jane_doe123@", "1234567890", "abc123",
    "Jane Doe", "jane.doe@example.com", "jane.doe@domain", "9876543210", "xyz789",
    "Alice Smith", "alice.smith@example.com", "alice.smith@", "555-555-5555", "alice123",
    "Bob Johnson", "bob.johnson@example.com", "bob.johnson@", "444-444-4444", "bob456",
    "Charlie Brown", "charlie.brown@example.com", "charlie.brown@", "333-333-3333", "charlie789",
    "David Wilson", "david.wilson@example.com", "david.wilson@", "222-222-2222", "david123",
    "Eve Adams", "eve.adams@example.com", "eve.adams@", "111-111-1111", "eve456",
    "Frank Miller", "frank.miller@example.com", "frank.miller@", "000-000-0000", "frank789",
    "Grace Lee", "grace.lee@example.com", "grace.lee@", "999-999-9999", "grace123",
    "Hank Green", "hank.green@example.com", "hank.green@", "888-888-8888", "hank456",
    "Ivy White", "ivy.white@example.com", "ivy.white@", "777-777-7777", "ivy789",
    "Jack Black", "jack.black@example.com", "jack.black@", "666-666-6666", "jack123",
    "Kate Brown", "kate.brown@example.com", "kate.brown@", "555-555-5555", "kate456",
    "Leo King", "leo.king@example.com", "leo.king@", "444-444-4444", "leo789",
    "Mia Queen", "mia.queen@example.com", "mia.queen@", "333-333-3333", "mia123",
    "Nick Stone", "nick.stone@example.com", "nick.stone@", "222-222-2222", "nick456",
    "Olivia Young", "olivia.young@example.com", "olivia.young@", "111-111-1111", "olivia789",
    "Paul Walker", "paul.walker@example.com", "paul.walker@", "000-000-0000", "paul123",
    "Quinn Hall", "quinn.hall@example.com", "quinn.hall@", "999-999-9999", "quinn456",
    "Rachel Adams", "rachel.adams@example.com", "rachel.adams@", "888-888-8888", "rachel789"
]
data.extend([
    "cat", "dog", "bat", "tree", "house", "apple", "pear", "book", "fish", "star",
    "moon", "sun", "rain", "snow", "wind", "fire", "rock", "sand", "wave", "leaf",
    "so","as","is","it","at","to","be","me","we","he","Roshan","Raj","Rahul","Ravi","Rahim","Rajesh","Ramesh","Rajeev","Rajendra","Rajiv",
])

import re

expression=r"^[a-zA-Z][\._a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|net|org|in)$"

for item in data:
    if re.search(expression, item):
        print(item)
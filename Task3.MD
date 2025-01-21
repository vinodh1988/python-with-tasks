### User and Permissions

- Create a new user `db_user`.
- Grant `CONNECT` permission to `db_user`.
- Grant `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, and `SELECT` permissions to `db_user` on all objects in the `books` database.

in the books database create the following things 
## Database Schema and Operations

### Create Tables with Constraints

#### Authors
- `author_id` (Primary Key, Auto Increment)
- `name` (Not Null)
- `email` (Unique, Not Null)

#### Books
- `book_id` (Primary Key, Auto Increment)
- `title` (Not Null)
- `genre`
- `publish_date`
- `author_id` (Foreign Key referencing `Authors.author_id`)

#### Publishers
- `publisher_id` (Primary Key, Auto Increment)
- `name` (Not Null)
- `address`

#### BookPublisher
- `book_id` (Foreign Key referencing `Books.book_id`)
- `publisher_id` (Foreign Key referencing `Publishers.publisher_id`)
- Primary Key (`book_id`, `publisher_id`)

#### Customers
- `customer_id` (Primary Key, Auto Increment)
- `name` (Not Null)
- `email` (Unique, Not Null)
- `date_of_birth`
- `membership_level` (Enum: 'Silver', 'Gold', 'Platinum')

#### Orders
- `order_id` (Primary Key, Auto Increment)
- `order_date` (Not Null)
- `customer_id` (Foreign Key referencing `Customers.customer_id`)
- `book_id` (Foreign Key referencing `Books.book_id`)

#### Addresses
- `address_id` (Primary Key, Auto Increment)
- `customer_id` (Foreign Key referencing `Customers.customer_id`, Unique)
- `street`
- `city`
- `postal_code`

#### Categories
- `category_id` (Primary Key, Auto Increment)
- `category_name` (Not Null)

#### BookCategories
- `book_id` (Foreign Key referencing `Books.book_id`)
- `category_id` (Foreign Key referencing `Categories.category_id`)
- Primary Key (`book_id`, `category_id`)

#### Reviews
- `review_id` (Primary Key, Auto Increment)
- `book_id` (Foreign Key referencing `Books.book_id`)
- `review_text`
- `rating` (Check constraint to ensure rating is between 1 and 5)

### Insert Records

- Insert 3 records into the `Authors` table.
- Insert 4 records into the `Books` table.
- Insert 2 records into the `Publishers` table.
- Insert 4 records into the `BookPublisher` table to establish relationships.
- Insert 3 records into the `Customers` table.
- Insert 3 records into the `Orders` table.
- Insert 3 records into the `Addresses` table, ensuring each customer has one address.
- Insert 3 records into the `Categories` table.
- Insert 4 records into the `BookCategories` table to establish relationships.
- Insert 3 records into the `Reviews` table.

### Alter Table

- Add a new column `isbn` (Unique) to the `Books` table.
- Add a column `phone_number` (Unique) to the `Customers` table.
- Add a foreign key constraint `publisher_id` to the `Books` table, referencing `Publishers.publisher_id`.
- Add a check constraint to the `Customers` table to ensure `date_of_birth` is in the past.
- Add a column `discount` to the `Orders` table with a default value of 0.
- Modify the `membership_level` column in the `Customers` table to include an additional level 'Diamond'.
- Add a foreign key constraint `book_id` to the `Reviews` table, referencing `Books.book_id`.
- Add a unique constraint on the combination of `name` and `author_id` in the `Books` table to prevent duplicate books by the same author.
- Change the `rating` column in the `Reviews` table to ensure it can only have integer values.
- Add a foreign key constraint `category_id` to the `Books` table, referencing `Categories.category_id`.

### Update Records

- Update the email address of the author with `author_id` 1.
- Update the membership level of the customer with `customer_id` 2.
- Update the address of the customer with `customer_id` 3.
- Update the genre of the book with `book_id` 2.
- Update the rating of a review with `review_id` 1 to 4.
- Update the discount of the order with `order_id` 1 to 10%.
- Update the publisher of the book with `book_id` 3 to `publisher_id` 2.
- Update the phone number of the customer with `customer_id` 1.
- Update the title of the book with `book_id` 4.
- Update the category of the book with `book_id` 1 to `category_id` 3.

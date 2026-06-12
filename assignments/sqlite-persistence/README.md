# 📘 Assignment: SQLite Database Persistence

## 🎯 Objective

Learn how to use Python with SQLite to save, update, and query data in a local database. Students will build a simple CRUD app that stores items in a SQLite table.

## 📝 Tasks

### 🛠️ Initialize the SQLite database

#### Description
Create a SQLite database file and set up a table for storing item records.

#### Requirements
Completed program should:

- Use Python's `sqlite3` module to connect to `items.db`
- Create a table named `items` with columns `id`, `name`, `description`, and `price`
- Insert at least three sample rows if the table is empty
- Print all rows from the table after initialization

### 🛠️ Add and update item records

#### Description
Write functions to add new items and update the price of existing items.

#### Requirements
Completed program should:

- Define a function `add_item(name, description, price)` that inserts a new item into the database
- Define a function `update_price(item_id, new_price)` that updates the price for the specified item
- Print a helpful message if the item ID is not found

### 🛠️ Delete and query items

#### Description
Implement the ability to delete items and retrieve a single item by ID.

#### Requirements
Completed program should:

- Define a function `delete_item(item_id)` that removes an item from the database
- Define a function `get_item(item_id)` that returns a single item by its ID
- Print a message when an item is not found

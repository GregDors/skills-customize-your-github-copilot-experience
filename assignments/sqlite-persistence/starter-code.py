import sqlite3
from sqlite3 import Error

DB_FILE = "items.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);
"""

sample_items = [
    ("Notebook", "A spiral notebook for notes", 3.99),
    ("Pencil", "A graphite pencil", 0.99),
    ("Backpack", "A school backpack", 29.99),
]


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None


def initialize_database():
    conn = create_connection(DB_FILE)
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM items")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany("INSERT INTO items (name, description, price) VALUES (?, ?, ?)", sample_items)
        conn.commit()

    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()


def add_item(name, description, price):
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
            (name, description, price),
        )
        conn.commit()
        conn.close()
        print(f"Added item: {name}")


def update_price(item_id, new_price):
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET price = ? WHERE id = ?", (new_price, item_id))
        conn.commit()
        if cursor.rowcount == 0:
            print("Item not found")
        else:
            print(f"Updated item {item_id} price to {new_price}")
        conn.close()


def delete_item(item_id):
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Item not found")
        else:
            print(f"Deleted item {item_id}")
        conn.close()


def get_item(item_id):
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            print(row)
            return row
        print("Item not found")
        return None


if __name__ == "__main__":
    initialize_database()
    add_item("Eraser", "A small eraser", 0.49)
    update_price(1, 4.49)
    get_item(2)
    delete_item(3)

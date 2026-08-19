import sqlite3

conn = sqlite3.connect("people.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS orders;

CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    person_id INTEGER NOT NULL,
    item TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (person_id) REFERENCES people(id)
);

INSERT INTO people (name, age, city) VALUES
    ('Alice', 25, 'Bengaluru'),
    ('Rahul', 30, 'Mumbai'),
    ('Sneha', 28, 'Bengaluru'),
    ('Kiran', 35, 'Delhi'),
    ('Neha', 22, 'Mumbai');

INSERT INTO orders (person_id, item, amount) VALUES
    (1, 'Laptop', 55000),
    (1, 'Mouse', 800),
    (2, 'Keyboard', 2000),
    (3, 'Monitor', 12000),
    (3, 'Laptop', 60000),
    (5, 'Headphones', 3000);
""")

conn.commit()
conn.close()
print("Database created.")
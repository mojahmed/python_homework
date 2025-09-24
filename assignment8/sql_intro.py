import sqlite3

try:
    # Task 1: Connect to database
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")  # enforce foreign keys
    c = conn.cursor()
    print("Database connected.\n")

    # Clear old data to prevent duplicates
    c.execute("DELETE FROM subscriptions")
    c.execute("DELETE FROM magazines")
    c.execute("DELETE FROM subscribers")
    c.execute("DELETE FROM publishers")
    conn.commit()
    print("Old data cleared.\n")

    # Task 2: Create tables
    c.execute("CREATE TABLE IF NOT EXISTS publishers (id INTEGER PRIMARY KEY, name TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS magazines (id INTEGER PRIMARY KEY, name TEXT, publisher_id INTEGER, FOREIGN KEY(publisher_id) REFERENCES publishers(id))")
    c.execute("CREATE TABLE IF NOT EXISTS subscribers (id INTEGER PRIMARY KEY, name TEXT, address TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS subscriptions (id INTEGER PRIMARY KEY, subscriber_id INTEGER, magazine_id INTEGER, expiration_date TEXT, FOREIGN KEY(subscriber_id) REFERENCES subscribers(id), FOREIGN KEY(magazine_id) REFERENCES magazines(id))")
    print("Tables created.\n")

    # Task 3: Insert sample data using parameterized queries

    # Publishers
    publishers = ["Tech World", "Health Plus", "Travel Life"]
    for p in publishers:
        c.execute("INSERT INTO publishers (name) VALUES (?)", (p,))

    # Magazines
    magazines = [("Gadget Weekly", 1), ("Wellness Today", 2), ("Adventure Guide", 3)]
    for m in magazines:
        c.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", m)

    # Subscribers
    subscribers = [("John", "123 Main St"), ("Ahmed", "45 King Rd"), ("Mary", "78 Elm St")]
    for s in subscribers:
        c.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", s)

    # Subscriptions
    subscriptions = [(1, 1, "2025-12-31"), (2, 2, "2025-11-15"), (3, 3, "2025-10-01")]
    for sub in subscriptions:
        c.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", sub)

    conn.commit()
    print("Sample data added.\n")

    # Task 4: SQL Queries

    # 1. All subscribers
    print("SUBSCRIBERS:")
    c.execute("SELECT * FROM subscribers")
    for row in c.fetchall():
        print(row)
    print()

    # 2. All magazines sorted by name
    print("MAGAZINES (sorted by name):")
    c.execute("SELECT * FROM magazines ORDER BY name")
    for row in c.fetchall():
        print(row)
    print()

    # 3. Magazines for a particular publisher (Tech World)
    print("MAGAZINES for publisher 'Tech World':")
    c.execute("""
        SELECT magazines.id, magazines.name, publishers.name
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.id
        WHERE publishers.name = ?
    """, ("Tech World",))
    for row in c.fetchall():
        print(row)
    print()

except sqlite3.Error as e:
    print("Something went wrong:", e)

finally:
    if conn:
        conn.close()
        print("Connection closed.")

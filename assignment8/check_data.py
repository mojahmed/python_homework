import sqlite3

try:
    conn = sqlite3.connect("../db/magazines.db")
    cur = conn.cursor()
    print("Connected to database.\n")

    #  each table
    tables = ["publishers", "magazines", "subscribers", "subscriptions"]
    for table in tables:
        print(f"--- {table.upper()} ---")
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print()

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if conn:
        conn.close()
        print("Connection closed.")

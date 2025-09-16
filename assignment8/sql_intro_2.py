# Task 5: Read Data into a DataFrame
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("../db/lesson.db")
print("Connected to database.\n")

# Create tables and add sample data
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, product_name TEXT, price REAL)")
c.execute("CREATE TABLE IF NOT EXISTS line_items (line_item_id INTEGER PRIMARY KEY, order_id INTEGER, product_id INTEGER, quantity INTEGER, FOREIGN KEY(product_id) REFERENCES products(product_id))")

products = [("Laptop", 1000), ("Smartphone", 500), ("Tablet", 300)]
for p in products:
    c.execute("INSERT OR IGNORE INTO products (product_name, price) VALUES (?, ?)", p)

line_items = [(1, 1, 2), (2, 2, 1), (3, 3, 3)]
for li in line_items:
    c.execute("INSERT OR IGNORE INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)", li)

conn.commit()
print("Tables and data added.\n")

# Read data into DataFrame
df = pd.read_sql_query("""
SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
""", conn)


print("First 5 rows:")
print(df.head(), "\n")

# Add total column
df['total'] = df['quantity'] * df['price']
print("DataFrame with 'total':")
print(df.head(), "\n")

# Group by product_id
summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).rename(columns={'line_item_id':'order_count', 'total':'total_sales'}).reset_index()

# Sort by product_name
summary = summary.sort_values('product_name')

print("Summary by product:")
print(summary.head(), "\n")

# Write summary to CSV
summary.to_csv("../order_summary.csv", index=False)
print("Summary written to order_summary.csv")

# Close connection
conn.close()
print("Connection closed.")

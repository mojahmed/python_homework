# Task 1: Total price per order
import sqlite3

def main():
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")  #  foreign key 
    cursor = conn.cursor()

  
    # Task 1: Total price per order
    
    query_task1 = """
    SELECT 
        orders.order_id,
        orders.customer_name,
        COALESCE(SUM(products.price * line_items.quantity), 0) AS total_price
    FROM orders
    LEFT JOIN line_items ON orders.order_id = line_items.order_id
    LEFT JOIN products ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
    ORDER BY orders.order_id
    LIMIT 5;
    """
    cursor.execute(query_task1)
    results_task1 = cursor.fetchall()

    print("Task 1: Total")
    for row in results_task1:
        order_id, customer_name, total_price = row
        print(f"Order {order_id} ({customer_name}): ${total_price:.2f}")

    # ------------------------------------------
    
    
    # Task 2: Average order price per customer
    
    query_task2 = """
    SELECT 
        orders.customer_name,
        AVG(order_totals.total_price) AS average_total_price
    FROM orders
    LEFT JOIN (
        SELECT 
            orders.order_id,
            orders.customer_name AS customer_id_b,
            COALESCE(SUM(products.price * line_items.quantity), 0) AS total_price
        FROM orders
        LEFT JOIN line_items ON orders.order_id = line_items.order_id
        LEFT JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
    ) AS order_totals
    ON orders.customer_name = order_totals.customer_id_b
    GROUP BY orders.customer_name;
    """
    cursor.execute(query_task2)
    results_task2 = cursor.fetchall()

    print("\nTask 2: Average")
    for row in results_task2:
        customer_name, avg_total = row
        print(f"{customer_name}: ${avg_total:.2f}")



    # ------------------------------------------
    
    
    # Task 3: Insert a new order with line_items
   
    try:
       
        new_customers = ["Ali", "Sara", "Omar"]

        for customer in new_customers:
            # Insert a new order for the customer
            cursor.execute(
                "INSERT INTO orders (customer_name) VALUES (?) RETURNING order_id",
                (customer,)
            )
            order_id = cursor.fetchone()[0]

            # Get 5 least expensive products 
            cursor.execute("""
            SELECT product_id 
            FROM products 
            GROUP BY product_name 
            ORDER BY MIN(price) ASC 
            LIMIT 5
            """)
            product_ids = [row[0] for row in cursor.fetchall()]

            # Insert line_items for the new order (10 quantity each)
            for pid in product_ids:
                cursor.execute(
                    "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                    (order_id, pid, 10)
                )

         
            conn.commit()

            # Confirm insertion
            cursor.execute("""
            SELECT line_item_id, quantity, products.product_name
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id
            WHERE order_id = ?
            """, (order_id,))
            results_task3 = cursor.fetchall()

            print(f"\nTask 3: Inserted line_items for new order ({customer})")
            for row in results_task3:
                line_item_id, quantity, product_name = row
                print(f"Line Item {line_item_id}: {quantity} x {product_name}")

    except Exception as e:
        conn.rollback()
        print("Task 3 transaction failed:", e)

   
    # Show last two orders
   
    cursor.execute("""
    SELECT order_id, customer_name
    FROM orders
    ORDER BY order_id DESC
    LIMIT 2
    """)
    last_orders = cursor.fetchall()

    print("\nLast two orders added:")
    for row in last_orders:
        print(f"Order {row[0]}: {row[1]}")
        
        

    # ------------------------------------------
    
    
    # Task 4: Employees with more than 5 orders

    query_task4 = """
    SELECT 
        employees.employee_id,
        employees.first_name,
        employees.last_name,
        COUNT(orders.order_id) AS order_count
    FROM employees
    JOIN orders ON employees.employee_id = orders.employee_id
    GROUP BY employees.employee_id
    HAVING COUNT(orders.order_id) > 5;
    """
    cursor.execute(query_task4)
    results_task4 = cursor.fetchall()

    print("\nTask 4: Employees with more than 5 orders")
    for row in results_task4:
        employee_id, first_name, last_name, order_count = row
        print(f"Employee {employee_id}: {first_name} {last_name} – {order_count} orders.")

    conn.close()


if __name__ == "__main__":
    main()

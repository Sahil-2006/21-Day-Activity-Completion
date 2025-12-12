import sqlite3
from datetime import datetime, timedelta

# ---------------------------------------
# 1. Connect to SQLite database
# ---------------------------------------
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# ---------------------------------------
# 2. Create tables
# ---------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    last_purchase_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    amount REAL,
    order_date TEXT,
    delivery_status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL,
    join_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    last_login TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER
)
""")

conn.commit()

# ---------------------------------------
# 3. Insert Sample Data
# ---------------------------------------

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", [
    (1, "Amit", (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")),
    (2, "Riya", (datetime.now() - timedelta(days=40)).strftime("%Y-%m-%d")),
    (3, "Sam", (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"))
])

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 1, 101, 500, "2025-12-01", "Delivered"),
    (2, 1, 102, 300, "2025-12-05", "Pending"),
    (3, 2, 101, 400, "2025-11-15", "Delivered"),
    (4, 3, 103, 250, "2025-12-10", "Pending")
])

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (1, "John", 50000, "2024-03-15"),
    (2, "Neha", 70000, "2024-08-10"),
    (3, "Rahul", 45000, "2023-12-20")
])

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, "alpha", (datetime.now() - timedelta(days=100)).strftime("%Y-%m-%d")),
    (2, "beta", (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d")),
    (3, "gamma", (datetime.now() - timedelta(days=200)).strftime("%Y-%m-%d"))
])

cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?)", [
    (101, "Shoes", 0),
    (102, "Shirt", 10),
    (103, "Watch", -1),
])

conn.commit()

# ---------------------------------------
# 4. Run All 10 Real-World SQL Queries
# ---------------------------------------

print("\n1️⃣ Customers who purchased in last 30 days")
cursor.execute("""
SELECT * FROM customers
WHERE last_purchase_date >= DATE('now', '-30 days')
""")
print(cursor.fetchall())

print("\n2️⃣ Total revenue for current month")
cursor.execute("""
SELECT SUM(amount) FROM orders
WHERE strftime('%m', order_date) = strftime('%m', 'now')
  AND strftime('%Y', order_date) = strftime('%Y', 'now')
""")
print(cursor.fetchone())

print("\n3️⃣ Employees with salary > company average")
cursor.execute("""
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
""")
print(cursor.fetchall())

print("\n4️⃣ Top 5 most selling products")
cursor.execute("""
SELECT product_id, COUNT(*) AS total_sales
FROM orders
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5
""")
print(cursor.fetchall())

print("\n5️⃣ Users who haven’t logged in for 90 days")
cursor.execute("""
SELECT * FROM users
WHERE last_login < DATE('now', '-90 days')
""")
print(cursor.fetchall())

print("\n6️⃣ Total orders placed by each customer")
cursor.execute("""
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
""")
print(cursor.fetchall())

print("\n7️⃣ Orders not yet delivered")
cursor.execute("""
SELECT * FROM orders
WHERE delivery_status = 'Pending'
""")
print(cursor.fetchall())

print("\n8️⃣ Employees who joined between 2024")
cursor.execute("""
SELECT name, join_date FROM employees
WHERE join_date BETWEEN '2024-01-01' AND '2024-12-31'
""")
print(cursor.fetchall())

print("\n9️⃣ Customers who bought product 101")
cursor.execute("""
SELECT c.customer_id, c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.product_id = 101
""")
print(cursor.fetchall())

print("\n🔟 Products out of stock")
cursor.execute("""
SELECT product_id, product_name
FROM inventory
WHERE quantity <= 0
""")
print(cursor.fetchall())

# ---------------------------------------
# 5. Close connection
# ---------------------------------------
conn.close()

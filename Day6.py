1. Get all customers who made a purchase in the last 30 days
sql
Copy code
SELECT *
FROM customers
WHERE last_purchase_date >= DATE('now', '-30 days');
Use Case: E-commerce "active customers" list.

2. Find total revenue for the current month
sql
Copy code
SELECT SUM(amount) AS total_revenue
FROM orders
WHERE strftime('%m', order_date) = strftime('%m', 'now')
  AND strftime('%Y', order_date) = strftime('%Y', 'now');
Use Case: Monthly sales dashboard.

3. List employees with salaries greater than the company average
sql
Copy code
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
Use Case: HR benchmarking, salary analysis.

4. Find the top 5 most selling products
sql
Copy code
SELECT product_id, COUNT(*) AS total_sales
FROM orders
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5;
Use Case: Analytics, product insights.

5. Show all users who haven’t logged in for 90 days
sql
Copy code
SELECT *
FROM users
WHERE last_login < DATE('now', '-90 days');
Use Case: Identify inactive users for re-engagement.

6. Get total number of orders placed by each customer
sql
Copy code
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id;
Use Case: Customer loyalty scoring.

7. Find orders that have not yet been delivered
sql
Copy code
SELECT *
FROM orders
WHERE delivery_status = 'Pending';
Use Case: Logistics, delivery dashboard.

8. Retrieve employees who joined between two dates
sql
Copy code
SELECT name, join_date
FROM employees
WHERE join_date BETWEEN '2024-01-01' AND '2024-12-31';
Use Case: HR filters.

9. Find customers who bought a specific product
sql
Copy code
SELECT c.customer_id, c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.product_id = 101;
Use Case: Marketing: target customers of a specific category.

10. Find products that are out of stock
sql
Copy code
SELECT product_id, product_name
FROM inventory
WHERE quantity <= 0;
Use Case: Inventory management alerts.
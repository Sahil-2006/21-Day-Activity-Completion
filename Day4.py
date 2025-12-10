"""
1. Import the database library
For SQLite (comes built-in):
import sqlite3

2. Connect to a database
If the file doesn't exist, Python will create it.
conn = sqlite3.connect("mydb.db")

3. Create a cursor
A cursor is like a pen used to write SQL.
cursor = conn.cursor()

4. Write your SQL command as a STRING
Example:
sql = "CREATE TABLE students (id INTEGER, name TEXT)"

5. Tell Python to execute the SQL
cursor.execute(sql)

6. If you INSERT/UPDATE/DELETE → SAVE CHANGES
conn.commit()

7. If you SELECT → get the results
rows = cursor.fetchall()
print(rows)

8. Close the connection
conn.close()
"""
import sqlite3

# 1. connect
conn = sqlite3.connect("mydb.db")

# 2. cursor
cursor = conn.cursor()

# 3. write SQL
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")

# 4. insert
cursor.execute("INSERT INTO users VALUES (1, 'Sahil')")
conn.commit()

# 5. select
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# 6. close
conn.close()

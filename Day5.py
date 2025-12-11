import sqlite3

# 1. connect
conn = sqlite3.connect("mydb.db")

# 2. cursor
cursor = conn.cursor()

# 3. create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    name TEXT
)
""")

# 4. insert sample data
cursor.execute("INSERT INTO users VALUES (1, 'Sahil')")
cursor.execute("INSERT INTO users VALUES (2, 'Sam')")
cursor.execute("INSERT INTO users VALUES (3, 'Riya')")
cursor.execute("INSERT INTO users VALUES (4, 'Rahul')")
conn.commit()

# -------------------------
#    SQL FILTERING
# -------------------------

print("\n1. WHERE id > 2")
cursor.execute("SELECT * FROM users WHERE id > 2")
print(cursor.fetchall())

print("\n2. ORDER BY name (ascending)")
cursor.execute("SELECT * FROM users ORDER BY name ASC")
print(cursor.fetchall())

print("\n3. LIKE 'Sa%'  (names starting with 'Sa')")
cursor.execute("SELECT * FROM users WHERE name LIKE 'Sa%'")
print(cursor.fetchall())

print("\n4. LIKE '%a'  (names ending with 'a')")
cursor.execute("SELECT * FROM users WHERE name LIKE '%a'")
print(cursor.fetchall())

# 6. close
conn.close()
# Import the package
import sqlite3

# NOTE: sqlite3 is case sensitive

# Create a new database or connect to an existing one
conn = sqlite3.connect('customer.db')

# Create a cursor
crsr = conn.cursor()

# Query the database and limiting the query to fetch only two records
crsr.execute("""
    SELECT rowid, * FROM customers LIMIT 2
""")

# Fetch all records
print(crsr.fetchall())

# Close the connection
conn.close()
# Import the package
import sqlite3

# NOTE: sqlite3 is case sensitive

# Create a new database or connect to an existing one
conn = sqlite3.connect('customer.db')

# Create a cursor
crsr = conn.cursor()

# Delete the entire table
crsr.execute("""
    DROP TABLE customers
""")

# Commit the changes
conn.commit()

# Try to fetch the records from table, should throw an error
crsr.execute("SELECT * FROM customers")

# Fetch all records
print(crsr.fetchall())

# Close the connection
conn.close()
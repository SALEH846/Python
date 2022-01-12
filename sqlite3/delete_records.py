# Import the package
import sqlite3

# NOTE: sqlite3 is case sensitive

# Create a new database or connect to an existing one
conn = sqlite3.connect('customer.db')

# Create a cursor
crsr = conn.cursor()

# Query the database
print("---------------Before Deleting-----------------")
crsr.execute("SELECT rowid, * FROM customers")

# Fetch all records
print(crsr.fetchall())

# Delete the record
crsr.execute("""
    DELETE FROM customers WHERE rowid == 2
""")

# Commit the changes
conn.commit()

# Query the database
print("---------------After Deleting-----------------")
crsr.execute("SELECT rowid, * FROM customers")

# Fetch all records
print(crsr.fetchall())

# Close the connection
conn.close()
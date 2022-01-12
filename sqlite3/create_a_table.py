# Import the package
import sqlite3

# NOTE: sqlite3 is case sensitive

# Create a new database or connect to an existing one
conn = sqlite3.connect('customer.db')

# Create a cursor
crsr = conn.cursor()

# Now, create a table
crsr.execute("""
    CREATE TABLE customers (
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
""")

# sqlite3 has just 5 datatypes
# 1. NULL
# 2. INTEGER
# 3. REAL
# 4. TEXT
# 5. BLOB

# Commit the changes
conn.commit()

# Close the connection
conn.close()
# Import the package
import sqlite3

# NOTE: sqlite3 is case sensitive

# Create a new database or connect to an existing one
conn = sqlite3.connect('customer.db')

# Create a cursor
crsr = conn.cursor()

crsr.execute("""
    INSERT INTO customers VALUES (
        'Mary',
        'Brown',
        'mary@elder.com'
    )
""")


# Commit the changes
conn.commit()

# Close the connection
conn.close()
# Import the package
import sqlite3

# NOTE: sqlite3 is case sensitive

# Create a new database or connect to an existing one
conn = sqlite3.connect('customer.db')

# Create a cursor
crsr = conn.cursor()

group_of_customers = [
    ('Wes', 'White', 'wes@white.com'),
    ('Alex', 'Hales', 'alex@ecb.co.uk'),
    ('John', 'Doe', 'doe@fake.com')
]

crsr.executemany("INSERT INTO customers VALUES (?, ?, ?)", group_of_customers)
# NOTE: '?' is a placeholder

# Commit the changes
conn.commit()

# Close the connection
conn.close()
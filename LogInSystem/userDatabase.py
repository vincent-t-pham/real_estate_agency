# This file is to create the user database
# A user will have a username and a password
# Temporary proof of concept

import sqlite3

conn = sqlite3.connect('users.db')

c = conn.cursor()

# Create the table
c.execute("""CREATE TABLE IF NOT EXISTS users (
             username text,
             password text
         )""")

c.execute("SELECT * FROM users")
if not c.fetchall():
    print("pain")

# Save changes
conn.commit()

# Close connections
conn.close()
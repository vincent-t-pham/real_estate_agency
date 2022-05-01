# This file is to create the user database
# A user will have a username and a password
# Temporary proof of concept

import sqlite3

conn = sqlite3.connect('users.db')

c = conn.cursor()

c.execute("")

# Create the user table
c.execute("""CREATE TABLE IF NOT EXISTS users (
             username varchar(25) not null,
             password varchar(25) not null,
             primary key (username)
         )""")

c.execute("""CREATE TABLE IF NOT EXISTS admins (
             admin_username varchar(25) not null,
             primary key (admin_username),
             foreign key (admin_username) references users(username)
         )""")

# Save changes
conn.commit()

# Close connections
conn.close()
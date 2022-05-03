# This file is to create the user database
# A user will have a username and a password
# Temporary proof of concept

import sqlite3
import hashlib

# Function to encrypt a password
# Returns a hash for the password using SHA256 to generate hash
def encryptPassword(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

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

# add an admin
password = encryptPassword("admin123")
c.execute("INSERT INTO users VALUES('admin1', ?)", (password,))
c.execute("INSERT INTO admins VALUES('admin1')")

# Save changes
conn.commit()

# Close connections
conn.close()

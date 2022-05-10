# SJSU CMPE 138 Spring 2022 TEAM 11

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

# add the agents
password = encryptPassword("password")
c.execute("INSERT INTO users VALUES('0985820', ?)", (password,)) # Anthony Edward
c.execute("INSERT INTO users VALUES('0975482', ?)", (password,)) # Paul Rudd
c.execute("INSERT INTO users VALUES('0989589', ?)", (password,)) # Anakin Skywalker
c.execute("INSERT INTO users VALUES('0986289', ?)", (password,)) # Jesse Pinkman

# add the clients
c.execute("INSERT INTO users VALUES('anikha69', ?)", (password,)) # Anikha S
c.execute("INSERT INTO users VALUES('christineio', ?)", (password,)) # Christine Polly
c.execute("INSERT INTO users VALUES('stephenstrange', ?)", (password,)) # Stephen S
c.execute("INSERT INTO users VALUES('tony_s', ?)", (password,)) # Tony S

# add the owners
c.execute("INSERT INTO users VALUES('jimmy23', ?)", (password,)) # Jimmy W
c.execute("INSERT INTO users VALUES('walter07', ?)", (password,)) # Walter S
c.execute("INSERT INTO users VALUES('aaron98', ?)", (password,)) # Aaron P
c.execute("INSERT INTO users VALUES('hina87', ?)", (password,)) # Hina S

# Save changes
conn.commit()

# Close connections
conn.close()

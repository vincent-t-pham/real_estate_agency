# This file will include:
# functions to add users to the database
# functions to verify that usernames are unique
# functions to verify that username and password match

import sqlite3 as sql
from user import user

# Debugging function to print out all users and passwords
def utilGetAllUsers():
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    print(c.fetchall())

    conn.close()

# Function to add a user to the database
def signIn(user):
    if usernameIsUnique(user.username):
        conn = sql.connect('users.db')
        c = conn.cursor()

        c.execute("INSERT INTO users VALUES (?, ?)", (user.username, user.password))
        conn.commit()
        conn.close()
    else:
        print("Username already taken")

# Checks to see if the username is unique before adding to the database
def usernameIsUnique(username):
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT ? FROM users", (username))
    if not c.fetchall():
        conn.close()
        return True
    conn.close()
    return False


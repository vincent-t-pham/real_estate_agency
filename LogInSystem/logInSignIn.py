# This file will include:
# functions to add users to the database
# functions to verify that usernames are unique
# functions to verify that username and password match

import sqlite3 as sql
from user import User

# Debugging function to print out all users and passwords
def utilGetAllUsers():
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    print(c.fetchall())

    conn.close()

# Function to add a user to the database
# Returns True if sign in is successful
# Returns False if sign in is unsuccessful
def signIn(user):
    if usernameIsUnique(user.username):
        conn = sql.connect('users.db')
        c = conn.cursor()

        c.execute("INSERT INTO users VALUES (?, ?)", (user.username, user.password))
        conn.commit()
        conn.close()
        return True
    else:
        print("Username already taken")
        return False

# Checks to see if the username is unique before adding to the database
def usernameIsUnique(username):
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT ? FROM users", (username,))
    if not c.fetchall():
        conn.close()
        return True
    conn.close()
    return False

# Checks to see if the username exists in the users database
def usernameExists(username):
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT ? FROM users", (username,))
    if c.fetchall():
        conn.close()
        return True
    conn.close()
    return False

# Function to log in the user
# Returns true if the username and password is correct
# Returns false if username doesn't exist or if password is wrong
def logIn(user):
    if usernameExists(user.username):
        conn = sql.connect('users.db')
        c = conn.cursor()

        c.execute("""
            SELECT username
            FROM users
            WHERE username='?' AND password='?';
        """, (user.username, user.password))

        if not c.fetchone():
            print("Login Failed - Password incorrect")
            conn.close()
            return False
        else:
            print("Login Successful")
            conn.close()
            return True
    else:
        print("Username not found")
        return False


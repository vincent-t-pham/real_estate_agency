# This file will include:
# functions to add users to the database
# functions to verify that usernames are unique
# functions to verify that username and password match

from gc import collect
import sqlite3 as sql
from user import User
import hashlib

# Debugging function to print out all users and passwords
def utilGetAllUsers():
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users")
    print(c.fetchall())

    conn.close()

# Debugging function to delete all data
def utilDeleteAll():
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("DELETE FROM users")
    conn.commit()

    conn.close()
    
    print("All records deleted")

# Print line break for extra readability
def printLineBreak():
    print("\n***********************\n")

# Function to encrypt a password
# Returns a hash for the password using SHA256 to generate hash
def encryptPassword(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to add a user to the database
# Only returns true if the username is unique
# Returns True if sign in is successful
# Returns False if sign in is unsuccessful
def signIn(user):
    if usernameIsUnique(user.username):
        conn = sql.connect('users.db')
        # conn.set_trace_callback(print)
        c = conn.cursor()

        c.execute("INSERT INTO users VALUES (?, ?)", (user.username, user.password))
        conn.commit()
        conn.close()
        return True
    else:
        print("Username already taken")
        return False

# Checks to see if the username is unique before adding to the database
# Returns True if unique
# Returns False if not unique
def usernameIsUnique(username):
    conn = sql.connect('users.db')
    # conn.set_trace_callback(print)
    c = conn.cursor()

    # Select row with the username
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchall()
    # print(result)
    # If query is empty, that means username doesn't exist so it's unique
    if not result:
        conn.close()
        return True
    conn.close()
    return False

# Checks to see if the username exists in the users database
# Returns True if it exists
# Returns False if it doesn't exist
def usernameExists(username):
    conn = sql.connect('users.db')
    c = conn.cursor()

    # Select row with the username
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    # If the query is not empty, that means username exists
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

        # Select the row where the username and the password matches the input
        c.execute("""
            SELECT username
            FROM users
            WHERE username=? AND password=?;
        """, (user.username, user.password))

        # If query is empty, username or password is incorrect
        if not c.fetchone():
            print("Login Failed - Password incorrect")
            conn.close()
            return False
        else:
            conn.close()
            return True
    
    else:
        print("Username not found")
        return False

# Function that returns a user object with encrypted password
def collectUserInfo():
    username = input("Enter username: ")
    password = input("Enter password: ")
    encryptedPassword = encryptPassword(password)
    user = User(username, encryptedPassword)
    return user

# Returns the username which will be used to determine
# if a user is an agent, landlord, seller, client, or admin
def logInSignIn():
    print("Welcome to the real estate agency application")
    printLineBreak()
    success = False
    while(not success):
        print("Choose an option")
        print("[1] Sign up")
        print("[2] Log in")
        selection = input("Selection").lower().replace(" ", "")

        # Sign up for a new account
        # The only people that can sign up are:
        #   Landlords, Sellers, and Clients
        #   Only an Admin can add a new Agent
        if selection == 'signup' or selection == '1':
            timeOutCounter = 0
            while timeOutCounter < 4:
                user = collectUserInfo()
                if signIn(user):
                    print("Sign up successful")
                    print("Welcome {username}!".format(user.username))
                    return user.username
                else:
                    print("Sign up unsuccessful, try again\n")
                    if (3 - timeOutCounter) > 1:
                        print("%d attempts remaining" % (3 - timeOutCounter))
                    elif (3 - timeOutCounter) == 1:
                        print("1 attempt remaining")
                    timeOutCounter += 1

        # Log in to an existing account
        if selection == 'login' or selection == '2':
            timeOutCounter = 0
            while timeOutCounter < 4:
                user = collectUserInfo()
                if logIn(user):
                    print("Log in successful")
                    print("Welcome back, {username}!".format(user.username))

                    return user.username
                else:
                    print("Try Again\n")
                    if (3 - timeOutCounter) > 1:
                        print("%d attempts remaining" % (3 - timeOutCounter))
                    elif (3 - timeOutCounter) == 1:
                        print("1 attempt remaining")
                    timeOutCounter += 1
        
        # Invalid input
        else:
            print("That is an invalid option, try again")

        printLineBreak()
# This file is to create the user database
# A user will have a username and a password
# Temporary proof of concept

import sqlite3

conn = sqlite3.connect('/user.db')

c = conn.cursor()

c.execute("""CREATE TABLE users (
             username text,
             password text
         )""")

conn.commit()

conn.close()
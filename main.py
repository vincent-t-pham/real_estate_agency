import sqlite3

from table import c         #import cursor
from table import conn      #import connection

state = int(input("""
1. Account
2. Do nothing
"""))

if state==1:
    c.execute("SELECT * from Owner")
    result = c.fetchall()
    print(result)
elif state==2:
    print("You good for nothing.")

conn.close()


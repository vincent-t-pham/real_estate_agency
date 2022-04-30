import sqlite3
from functions import ownerInput

from table import c                         #import cursor
from table import conn                      #import connection

while(int(input("Login\n"))!=1):
    print('', end='')    
print('You''ve logged into (admin/user)')

state = int(input("""
1. Account
2. Do nothing
3. Test function
"""))

if state==1:                                #wut
    c.execute("SELECT * from Owner")
    result = c.fetchall()
    print(result)
elif state==2:
    print("You good for nothing.")
elif state==3:
    ownerInput()
    c.execute("SELECT * from Property")
    print(c.fetchall())
conn.close()


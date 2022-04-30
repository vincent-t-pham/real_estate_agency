from datetime import date
import sqlite3 as db

conn = db.connect("agency.db")
curr = conn.cursor()

#1. login, check username to get the usertype, Wanye
#2. if landlord
check =1
while check:
    c = int(input("Hello, you are a landlord\n1) Select an agent\n2) Document maintenance Records \n3) Exit\n"))
    if c == 1:
        selectqry = "select * from agent"
        curr.execute(selectqry)
        result = curr.fetchall()
        for record in result:
            print(record)
    elif c == 2:
        today = date.today()
        username = (input("Enter Name: ")) #shouldn't ask, auto generate
        record_id = int(input("Enter Id:")) #shouldn't ask, auto generate
        Maintenance_item = (input("Enter maintenance item: "))
        insert_qry = f"insert into Maintenance_Record values({username},'{record_id}',today,'{Maintenance_item}')"
        curr.execute(insert_qry)
        conn.commit()
    elif c == 3:
        print("Program Terminated")
        check = 0
print("Thank You!")

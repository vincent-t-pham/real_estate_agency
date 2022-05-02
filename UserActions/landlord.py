import sqlite3
# A Landlord can select an agent out of a list of available agents
    # Agent [1]: name goes here
def selectAgent():
    #Supposed to connect Owner to Landlord to Agent in SQL, needs an entry into Agent
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    c.execute("SELECT * From Agent")  
    print(c.fetchall())

# Application then prints out the agent information so client can contact them


# A Landlord can also document and manage maintainance records
    # Add new maintainance record
    # Delete records
    # Show all records
def maintenance():
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    select = int(input("""
    1. Add maintenance record
    2. Show all records""")
    if (select==1):
        username = input("Enter your username: ")
        recordID = input("Enter your record ID: ")
        date = input("Enter your date in YEAR-MONTH-DAY format: ")
        item = input("Enter the item being maintenanced: ")
        c.execute("INSERT OR REPLACE INTO Maintenance_Record VALUES (?, ?, ?, ?)", (username, recordID, date, item))
        conn.commit()
        conn.close()
    if (select==2):
        c.execute("SELECT * from Maintenance_Record")
        conn.close()






# A Seller can select an agent out of a list of available agents
    # Agent [1]: name goes here
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

def inputProperty():
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    location = input("Enter your property [location]: ")
    squareFoot = input("Enter your property [square footage]: ")
    lotSize = input("Enter your property [lot size]: ")
    numberofBeds = input("Enter your property [number of beds]: ")
    numberofBaths = input("Enter your property [number of baths]: ")
    properyType = input("Enter your property [type]: ")
    #agentID = input("Enter your property [agent ID]: ")
    openhouseDate = input("Enter your property [open house date]: ")
    streetAddress = input("Enter your property [street address]: ")
    city = input("Enter your property [city]: ")
    state = input("Enter your property [state]: ")
    zipCode = input("Enter your property [zipCode]: ")
    c.execute("INSERT OR REPLACE INTO Property VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", location, squareFoot, lotSize, numberofBeds, numberofBaths, propertyType, ))

def maintenance():
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    select = int(input("""
    1. Add maintenance record
    2. Show all records"""))
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
        print(c.fetchall())
        conn.close()

# Application then prints out the agent information so client can contact them

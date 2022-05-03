import sqlite3
# A Landlord can select an agent out of a list of available agents
    # Agent [1]: name goes here
def selectAgent():
    #Supposed to connect Owner to Landlord to Agent in SQL, needs an entry into Agent
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    c.execute("SELECT * From Agent")  
    result = c.fetchall()
    print("                        ******** AGENTS LIST ********")
    agents = printAgents(result)

# Application then prints out the agent information so client can contact them



# A Landlord can also document and manage maintainance records
    # Add new maintainance record
    # Delete records
    # Show all records
def maintenance(username):
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    select = int(input("1. Add maintenance record\n2. Show all records\nSelection: """))
    print()
    if (select==1):
        #Queries for the next largest maintenance record ID
        c.execute("SELECT Max(Record_ID) from Maintenance_Record")
        result = c.fetchall()
        recordIDs = printID(result)
        recordID = int(recordIDs[0]) + 1

        date = input("Enter your date in YEAR-MONTH-DAY format: ")
        item = input("Enter the item being maintenanced: ")
        c.execute("INSERT OR REPLACE INTO Maintenance_Record VALUES (?, ?, ?, ?)", (username, recordID, date, item))
        conn.commit()
        conn.close()
    if (select==2):
        c.execute("SELECT * from Maintenance_Record WHERE Username=? ", (username,))
        result = c.fetchall()
        print("                        ******** MAINTENANCE LIST ********")
        printRecords(result)
        conn.close()

def printAgents(result):
    count = 1
    for agent in result:
        print("Agent [{}]".format(count))
        print(agent)
        count+=1

    propertyIDs = [prop[0] for prop in result]
    return propertyIDs

def printRecords(result):
    count = 1
    for record in result:
        print("Record [{}]".format(count))
        print(record)
        count+=1

    propertyIDs = [prop[0] for prop in result]
    return propertyIDs

def printID(result):
    id = [record[0] for record in result]
    return id
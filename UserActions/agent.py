import sqlite3
# An Agent can add a new listing to manage
# This action will assume that the current agent is managing this property
# also assumes that the new propery will be available
# Listed date will be today's date
    # Property ID
    # Listed Date
    # Square foot
    # Lot size
    # Number of beds
    # Number of baths
    # street address
    # City
    # State
    # zip code
    # property type
    # owner username

def addListing(username):
    conn=sqlite3.connect('agency.db')
    c = conn.cursor()
    propertyID = input("Enter your property [ID]: ")
    listedDate = input("Enter your property [Listed Date]: ")
    squareFoot = input("Enter your property [square footage]: ")
    lotSize = input("Enter your property [lot size]: ")
    numberofBaths = input("Enter your property [number of baths]: ")
    numberofBeds = input("Enter your property [number of beds]: ")
    streetAddress = input("Enter your property [street address]: ")
    city = input("Enter your property [city]: ")
    state = input("Enter your property [state]: ")
    zipCode = input("Enter your property [zipCode]: ")
    propertyType = input("Enter your property [type]: ")
    agentID = username
    # openhouseDate = input("Enter your property [open house date]: ")
    ownerUsername = input("Enter your property [Owner Username]: ")
    availability = int(input("Is your property available? (1 for yes, 0 for no): "))
    c.execute("INSERT OR REPLACE INTO Property VALUES (?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,?, ?, ?, ?, ?)", (propertyID, listedDate, squareFoot, lotSize, numberofBaths, numberofBeds, streetAddress, city, state, zipCode, propertyType, agentID, '0000-00-00', ownerUsername, availability))
    conn.commit()
    conn.close()
    
def contractListing():
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    #***User inputs for the contract***
    agentID = input("Enter your agent ID: ")
    c.execute("SELECT * FROM Property where Agent_id=? ", (agentID, ))
    result = c.fetchall()
    propertyIDs = printProperties(result)
    ownerUsernames = printUsername(result)
    index = int(input("Enter the property you're interested in using: "))
    contractID= int(input("Enter contract ID: "))
    propType = input("Enter the property type (sale/rental): ")
    price = int(input("Enter the monthly costs: "))
    #Purchase date and lease date retrieved later?
    purchaseDate = input("Enter the purchase date: ")
    leaseStartDate = input("Enter the lease start date: ")
    clientUsername = input("Enter the client username: ")
    #***User inputs end***

    propertyID = propertyIDs[index-1]
    ownerUsername = ownerUsernames[index-1]
    c.execute("INSERT OR REPLACE INTO Contract VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (contractID, propType, price, purchaseDate, leaseStartDate, clientUsername, ownerUsername, propertyID, agentID))
    c.execute("SELECT * from Contract")
    print(c.fetchall())
    conn.commit()
    conn.close()

# An agent can bring a listing off the market
# Select properties that they're managing
def offMarket():
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    #Uncomment to view database before and after updating offmarket
    #c.execute("SELECT * from Property")
    #print(c.fetchall())

    propertyID = int(input("What is the ID of the property you're trying to take off the market?"))
    c.execute("UPDATE Property SET availability=0 WHERE property_id = ?", (propertyID,))
    print("Your property has been taken off the market!")
    #c.execute("SELECT * from Property")
    #print(c.fetchall())
    conn.commit()
    conn.close()

# An agent can scedule an open house
# Select a property
# Enter a date (date cannot be in the past)
def openHouse():
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    c.execute("SELECT * from Property")
    print(c.fetchall())
    
    propertyID = input("Open House: What is your property ID? ")
    openHouse = input("Open House: What day is the open house? (YEAR-MN-DY): ")
    c.execute("UPDATE Property SET Open_house_date=? WHERE property_id = ?", (openHouse, propertyID))
    c.execute("SELECT * from Property")
    print(c.fetchall())
    conn.commit()
    conn.close()

# Prints properties and returns a list of property IDs
def printProperties(result):
    count = 1
    for property in result:
        print("Property [{}]".format(count))
        print(property)
        count+=1

    propertyIDs = [prop[0] for prop in result]
    return propertyIDs

def printUsername(result):
    usernames = [prop[13] for prop in result]
    return usernames

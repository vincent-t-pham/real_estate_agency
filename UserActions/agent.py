import sqlite3
from datetime import date
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
    listedDate = date.today().isoformat()
    propertyID = input("Enter your property [ID]: ")
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
    ownerUsername = input("Enter your property [Owner Username]: ")
    availability = 0
    c.execute("INSERT OR REPLACE INTO Property VALUES (?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,?, ?, ?, ?, ?)", (propertyID, listedDate, squareFoot, lotSize, numberofBaths, numberofBeds, streetAddress, city, state, zipCode, propertyType, agentID, '0000-00-00', ownerUsername, availability))
    conn.commit()
    conn.close()
    
def contractListing(username):
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    #***User inputs for the contract***
    #Queries for existing Property data to be used 
    c.execute("SELECT * FROM Property where Agent_id=? ", (username, ))
    result = c.fetchall()
    propertyIDs = printProperties(result)
    ownerUsernames = printUsername(result)
    propTypes = printType(result)
    index = int(input("Enter the property you're interested in using: "))

    #Queries for Contract_ID to index as input for contractID
    c.execute("SELECT Max(Contract_ID) from Contract")
    result = c.fetchall()
    contractIDs = printContractID(result)
    contractID = int(contractIDs[0]) + 1

    price = int(input("Enter the monthly costs: "))
    purchaseDate = input("Enter the purchase date: ")
    leaseStartDate = input("Enter the lease start date: ")
    clientUsername = input("Enter the client username: ")
    #***User inputs end***

    propType = propTypes[index-1]
    propertyID = propertyIDs[index-1]
    ownerUsername = ownerUsernames[index-1]
    c.execute("UPDATE Property SET availability=0 WHERE property_id=?", (propertyID, ))
    c.execute("INSERT OR REPLACE INTO Contract VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (contractID, propType, price, purchaseDate, leaseStartDate, clientUsername, ownerUsername, propertyID, username))
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
def openHouse(username):
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    agentID = username
    c.execute("SELECT * FROM Property where Agent_id=? ", (agentID, ))
    result = c.fetchall()
    propertyIDs = printProperties(result)
    index = int(input("Enter the property that you're interested in: "))
    propertyID = propertyIDs[index-1]
    openHouse = input("Open House: What day is the open house? (YEAR-MN-DY): ")
    c.execute("UPDATE Property SET Open_house_date=? WHERE property_id = ?", (openHouse, propertyID))
    conn.commit()
    conn.close()

def viewProperties(username):
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    c.execute("SELECT * from Property WHERE Agent_id=?", (username, ))
    result = c.fetchall()
    print("                        ******** PROPERTIES LIST ********")
    properties = printProperties(result)
    conn.close()

def viewContracts(username):
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()

    c.execute("SELECT * from Contract WHERE Agent_id=?", (username, ))
    result = c.fetchall()
    print("                        ******** CONTRACTS LIST ********")
    contracts = printContracts(result)
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

def printContracts(result):
    count = 1
    for contract in result:
        print("Contract [{}]".format(count))
        print(contract)
        count+=1

    contractIDs = [contract[0] for contract in result]
    return contractIDs

def printUsername(result):
    usernames = [prop[13] for prop in result]
    return usernames

def printType(result):
    types = [prop[10] for prop in result]
    return types

def printContractID(result):
    id = [contract[0] for contract in result]
    return id
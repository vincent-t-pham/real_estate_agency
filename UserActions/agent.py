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

def addListing():
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
    agentID = input("Enter your property [agent ID]: ")
    openhouseDate = input("Enter your property [open house date]: ")
    ownerUsername = input("Enter your property [Owner Username]: ")
    availability = int(input("Is your property available? (1 for yes, 0 for no): "))
    c.execute("INPUT OR REPLACE INTO Property VALUES (?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,?, ?, ?, ?, ?)", propertyID, listedDate, squareFoot, lotSize, numberofBaths, numberofBeds, streetAddress, city, state, zipCode, propertyType, agentID, openhouseDate, ownerUsername, availability)
    conn.commit()
    

# An agent can bring a listing off the market
# Select properties that they're managing

# An agent can scedule an open house
# Select a property
# Enter a date (date cannot be in the past)

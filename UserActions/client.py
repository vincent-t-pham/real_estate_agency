# Client needs to choose if they want to buy or rent

# When chosen, prompt the client to choose how they want to search for property
    # Search using Location
    # Search using # Beds and Baths
    # Search using budget

# Print all search results in a readable format - all results must be on the market
    # Property [1]
        # City: x
        # Beds: y
        # Bath: z
        # etc
    # Property [2]
        # City: x
        # Beds: y
        # Bath: z
        # etc

# Prompt user to select a property (1, 2, 3, etc)

# Display property agent info

import sqlite3 as sql

# Search for a rental property by location and print agent info
def searchLocation_Rent():
    city = input("Which city do you want to search? ")

    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("""
            SELECT DISTINCT* 
            FROM property NATURAL JOIN contract  
            WHERE city = ? AND property_type = 'rental'
            """, (city,))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = input("Which property are you interested in? ")
    id = propertyIDs[index - 1]

    print("Here is the agent info for that property: ")
    print(findAgent(id))

# Search a property that's on sale by location and print agent info
def searchLocation_Buy():
    city = input("Which city do you want to search? ")

    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("""
            SELECT DISTINCT* 
            FROM property NATURAL JOIN contract  
            WHERE city = ? AND property_type = 'sale'
            """, (city,))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = input("Which property are you interested in? ")
    id = propertyIDs[index - 1]

    print("Here is the agent info for that property: ")
    print(findAgent(id))
    
# Search a rental property based on bed and bath and print agent info
def searchBedBath_rent():
    bed = input("Minimum number of bedrooms: ")
    bath = input("Minimum number of bathrooms: ")

    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("""
            SELECT DISTINCT * 
            FROM property NATURAL JOIN contract
            where Number_of_baths>=? and Number_of_beds>=? and property_type="rental";
            """, (bath, bed))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = input("Which property are you interested in? ")
    id = propertyIDs[index - 1]

    print("Here is the agent info for that property: ")
    print(findAgent(id))

# Search for a property that's on sale based on bed and bath and print agent info
def searchBedBath_rent():
    bed = input("Minimum number of bedrooms: ")
    bath = input("Minimum number of bathrooms: ")

    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("""
            SELECT DISTINCT * 
            FROM property NATURAL JOIN contract
            where Number_of_baths>=? and Number_of_beds>=? and property_type="sale";
            """, (bath, bed))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = input("Which property are you interested in? ")
    id = propertyIDs[index - 1]

    print("Here is the agent info for that property: ")
    print(findAgent(id))



# Prints properties and returns a list of property IDs
def printProperties(result):
    count = 1
    for property in result:
        print("Property [{}]".format(count))
        print(property)

    propertyIDs = [prop[0] for prop in result]
    return propertyIDs
    
# Returns agent info based on property ID
def findAgent(propertyID):
    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("""
            SELECT *
            FROM agent
            WHERE Agent_id in (SELECT Agent_id
            FROM property
            WHERE Property_id = ?)
            """, (propertyID))
    result = c.fetchall()
    conn.close()

    return result
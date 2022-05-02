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

###########################################################################################
# Search for a rental property by location and print agent info
def searchLocation_Rent():
    city = input("\nWhich city do you want to search? ")
    print()

    conn = sql.connect('agency.db')
    c = conn.cursor()
    #conn.set_trace_callback(print)
    c.execute("""
            SELECT *
            FROM property JOIN rental_property ON Property_id = Rental_property_id
            WHERE city = ? and Property_type = 'rental';
            """, (city,))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = int(input("\nWhich property are you interested in? "))
    id = propertyIDs[index - 1]
    print()

    print("\nHere is the agent info for that property: ")
    print(findAgent(id))

# Search a property that's on sale by location and print agent info
def searchLocation_Buy():
    city = input("\nWhich city do you want to search? ")
    print()

    conn = sql.connect('agency.db')
    c = conn.cursor()
    #conn.set_trace_callback(print)
    c.execute("""
            SELECT *
            FROM property JOIN sale_property ON Property_id = Sale_property_id
            WHERE city = ? and Property_type = 'sale';
            """, (city,))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = int(input("\nWhich property are you interested in? "))
    id = propertyIDs[index - 1]
    print()

    print("\nHere is the agent info for that property: ")
    print(findAgent(id))
###########################################################################################
    
###########################################################################################
# Search a rental property based on bed and bath and print agent info
def searchBedBath_Rent():
    bed = input("\nMinimum number of bedrooms: ")
    bath = input("Minimum number of bathrooms: ")
    print()

    conn = sql.connect('agency.db')
    c = conn.cursor()
    #conn.set_trace_callback(print)
    c.execute("""
            SELECT DISTINCT * 
            FROM property JOIN rental_property ON Property_id = Rental_property_id
            where Number_of_baths>=? and Number_of_beds>=? and property_type="rental"
            """, (bath, bed))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = int(input("\nWhich property are you interested in? "))
    id = propertyIDs[index - 1]
    print()

    print("\nHere is the agent info for that property: ")
    print(findAgent(id))

# Search for a property that's on sale based on bed and bath and print agent info
def searchBedBath_Buy():
    bed = input("\nMinimum number of bedrooms: ")
    bath = input("Minimum number of bathrooms: ")
    print()

    conn = sql.connect('agency.db')
    c = conn.cursor()
    #conn.set_trace_callback(print)
    c.execute("""
            SELECT DISTINCT * 
            FROM property JOIN sale_property ON Property_id = Sale_property_id
            where Number_of_baths>=? and Number_of_beds>=? and property_type="sale"
            """, (bath, bed))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = int(input("\nWhich property are you interested in? "))
    id = propertyIDs[index - 1]
    print()

    print("\nHere is the agent info for that property: ")
    print(findAgent(id))
###########################################################################################

###########################################################################################
# Search a rental property based on bed and bath and print agent info
def searchBudget_Rent():
    budget = input("\nWhat is your budget? ")
    print()

    conn = sql.connect('agency.db')
    c = conn.cursor()
    #conn.set_trace_callback(print)
    c.execute("""
            SELECT DISTINCT * 
            FROM property JOIN rental_property ON Property_id = Rental_property_id
            where Monthly_rent <= ? AND property_type = "rental"
            """, (budget,))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = int(input("\nWhich property are you interested in? "))
    id = propertyIDs[index - 1]
    print()

    print("\nHere is the agent info for that property: ")
    print(findAgent(id))

# Search for a property that's on sale based budget and print agent info
def searchBudget_Buy():
    budget = input("\nWhat is your budget? ")
    print()

    conn = sql.connect('agency.db')
    c = conn.cursor()
    #conn.set_trace_callback(print)
    c.execute("""
            SELECT DISTINCT * 
            FROM property JOIN sale_property ON Property_id = Sale_property_id
            where Listing_price <= ? AND property_type = "sale"
            """, (budget,))
    result = c.fetchall()
    conn.close()

    propertyIDs = printProperties(result)

    index = int(input("\nWhich property are you interested in? "))
    id = propertyIDs[index - 1]
    print()

    print("\nHere is the agent info for that property: ")
    print(findAgent(id))
###########################################################################################

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
    # conn.set_trace_callback(print)
    c.execute("""
            SELECT *
            FROM agent
            WHERE Agent_id in (SELECT Agent_id
            FROM property
            WHERE Property_id = ?)
            """, (propertyID,))
    result = c.fetchall()
    conn.close()

    return result
import sqlite3

from table import c
from table import conn

def ownerInput():
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
    #c.execute("INPUT OR REPLACE INTO Property VALUES (:location, :squareFoot, :lotSize, :numberofBeds, :numberofBaths, :propertyType, :openhouseDate, :streetAddress, :city, :state, :zipCode)" {'location': location, 'squareFoot': squareFoot, 'lotSize': lotSize, 'numberofBeds': numberofBeds, 'numberofBaths': numberofBaths, 'propertyType': propertyType, 'openhousedate': openhousedate, 'streetAddress': streetAddress, 'city': city, 'state': state, 'zipCode': zipCode})
    conn.commit()

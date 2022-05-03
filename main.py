from LogInSystem import logInSignIn as log
from UserActions import admin
from UserActions import client
from UserActions import agent
from UserActions import landlord
from UserActions import seller
import logging

# Logging File 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('database.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Get username
username = log.logInSignUp()

# Check if user is an admin
if log.isAdmin(username):
    while True:
        print("\nWelcome Admin {}".format(username))
        print("Select an operation:")
        print("[1] Create new agent")
        print("[2] Delete an agent")
        print("[3] Delete an owner")
        print("[4] Delete a client")
        print("[5] Quit")
        selection = input("Selection: ")

        if selection == '1':
            admin.addNewAgent()
        elif selection == '2':
            admin.deleteAgent()
        elif selection == '3':
            admin.deleteOwner()
        elif selection == '4':
            admin.deleteClient()
        elif selection == '5':
            print("Quiting program")
            logger.info("***User quit program***")
            break
        else:
            print("Invalid option, try again")

elif log.isAgent(username):
    while True:
        print("\nWelcome Agent {}".format(username))
        print("Select an operation:")
        print("[1] Add a listing property")
        print("[2] Create a contract")
        #print("[3] Take a property off the market")
        print("[3] Create an open house")
        print("[4] View my properties")
        print("[5] View my contracts")
        print("[6] Exit")
        selection = input("Selection: ")
        print()

        if selection=='1':
            agent.addListing(username)
        elif selection=='2':
            agent.contractListing(username)
        #if selection=='3':
        #    agent.offMarket()
        elif selection=='3':
            agent.openHouse(username)
        elif selection=='4':
            agent.viewProperties(username)
        elif selection=='5':
            agent.viewContracts(username)
        elif selection=='6':
            print("Quitting Program")
            logger.info("***User quit program***")
            break
        else:
            print("Invalid option, try again")
    pass

elif log.isClient(username):
    while True:
        print("\nWelcome Client {}".format(username))
        print("Select an operation:")
        print("[1] Buy")
        print("[2] Rent")
        print("[3] Quit")
        selection = input("Selection: ")
        print()

        if selection == '1':
            while True:
                print("\nHow would you like to search for a property?")
                print("[1] By City")
                print("[2] By Bed and Bath")
                print("[3] By Budget")
                print("[4] Return")
                selection2 = input("Selection: ")
                print()

                if selection2 == '1':
                    client.searchLocation_Buy()
                elif selection2 == '2':
                    client.searchBedBath_Buy()
                elif selection2 == '3':
                    client.searchBudget_Buy()
                elif selection2 == '4':
                    print("Returning")
                    break
                else:
                    print("Invalid option, try again")

        elif selection == '2':
            while True:
                print("\nHow would you like to search for a property?")
                print("[1] By City")
                print("[2] By Bed and Bath")
                print("[3] By Budget")
                print("[4] Return")
                selection2 = input("Selection: ")
                print()

                if selection2 == '1':
                    client.searchLocation_Rent()
                elif selection2 == '2':
                    client.searchBedBath_Rent()
                elif selection2 == '3':
                    client.searchBudget_Rent()
                elif selection2 == '4':
                    print("Returning")
                    break
                else:
                    print("Invalid option, try again")
                    
        elif selection == '3':
            print("Quiting program")
            logger.info("***User quit program***")
            break
        else:
            print("Invalid option, try again")
            
elif log.isSeller(username):
    while True:
        print("\nWelcome Seller {}".format(username))
        print("Select an operation:")
        print("[1] View agent information")
        print("[2] Quit")
        selection = input("Selection: ")
        print("\n")

        if selection=='1':
            seller.selectAgent()
        elif selection=='2':
            print("Quitting program")
            logger.info("***User quit program***")
            break
        else:
            print("Invalid option, try again")

    pass

elif log.isLandlord(username):
    while True:
        print("\nWelcome Landlord {}".format(username))
        print("Select an operation:")
        print("[1] View agent information")
        print("[2] Enter maintenance record")
        print("[3] Exit")
        selection = input("Selection: ")
        print("\n")

        if selection=='1':
            landlord.selectAgent()
        elif selection=='2':
            landlord.maintenance(username)
        elif selection=='3':
            print("Quitting program")
            logger.info("***User quit program***")
            break
        else:
            print("Invalid option, try again")
    pass

else:
    print("not done pls help")

from LogInSystem import logInSignIn as log
from UserActions import admin
from UserActions import client

# Get username
username = log.logInSignUp()

# Check if user is an admin
if log.isAdmin(username):
    while True:
        print("Welcome Admin {}".format(username))
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
            break
        else:
            print("Invalid option, try again")

elif log.isAgent(username):
    # Agent options
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
            break
        else:
            print("Invalid option, try again")
            
elif log.isSeller(username):
    # Seller options
    pass

elif log.isLandlord(username):
    # Landlord options
    pass

else:
    print("not done pls help")

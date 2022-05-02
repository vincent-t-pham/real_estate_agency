from LogInSystem import logInSignIn as log
from UserActions import admin
from UserActions import landlord

landlord.selectAgent()
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

        if selection == 1:
            admin.addNewAgent()
        elif selection == 2:
            admin.deleteAgent()
        elif selection == 3:
            admin.deleteOwner()
        elif selection == 4:
            admin.deleteClient()
        elif selection == 5:
            print("Quiting program")
            break
        else:
            print("Invalid option, try again")

elif log.isAgent(username):
    # Agent options
    pass
elif log.isClient(username):
    # Client options
    pass
elif log.isSeller(username):
    # Seller options
    pass
elif log.isLandlord(username):
    selectAgent()
    pass

landlord.selectAgent()

# This file will include me hoping and praying that this all works

from user import User
import logInSignIn as log

#################################################

def printLineBreak():
    print("\n***********************\n")

#################################################

print("Welcome to app thing")
printLineBreak()
success = False
while(not success):
    print("Choose an option [sign in] [log in]")
    firstChoice = input("Selection: ")
    firstChoice = firstChoice.lower()
    firstChoice = firstChoice.replace(" ", "")
    
    if firstChoice == 'signin':
        timeOutCounter = 0
        while timeOutCounter < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            if log.signIn(user):
                print("Sign In Successful")
                success = True
                break
            else:
                print("Log In Unsuccessful, Try Again")
                if (3 - timeOutCounter) > 1:
                    print("%d attempts remaining" % (3 - timeOutCounter))
                elif (3 - timeOutCounter) == 1:
                    print("1 attempt remaining")
                timeOutCounter += 1
                
    
    elif firstChoice == 'login':
        timeOutCounter = 0
        while timeOutCounter < 4:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            if log.logIn(user):
                print("Log In Successful")
                success = True
                break
            else:
                print("Log In Unsuccessful, Try Again")
                if (3 - timeOutCounter) > 1:
                    print("%d attempts remaining" % (3 - timeOutCounter))
                elif (3 - timeOutCounter) == 1:
                    print("1 attempt remaining")
                timeOutCounter += 1

    else:
        print("That is an invalid option, try again")

    printLineBreak()

log.utilGetAllUsers()
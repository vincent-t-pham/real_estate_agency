# This file will include me hoping and praying that this all works

from user import User
import logInSignIn as log
import hashlib

#################################################

def printLineBreak():
    print("\n***********************\n")

# Function to encrypt a password
# Returns a hash for the password using SHA256 to generate hash
def encryptPassword(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

#################################################

log.utilGetAllUsers()
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
        while timeOutCounter < 4:
            username = input("Enter username: ")
            password = input("Enter password: ")
            encryptedPassword = encryptPassword(password)
            user = User(username, encryptedPassword)
            if log.signIn(user):
                print("Sign In Successful")
                success = True
                break
            else:
                print("Sign In Unsuccessful, Try Again\n")
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
            encryptedPassword = encryptPassword(password)
            user = User(username, encryptedPassword)
            if log.logIn(user):
                print("Log In Successful")
                success = True
                break
            else:
                print("Try Again\n")
                if (3 - timeOutCounter) > 1:
                    print("%d attempts remaining" % (3 - timeOutCounter))
                elif (3 - timeOutCounter) == 1:
                    print("1 attempt remaining")
                timeOutCounter += 1

    elif firstChoice == 'delete':
        log.utilDeleteAll()
        success = True

    elif firstChoice == 'showall':
        log.utilGetAllUsers()
        success = True

    else:
        print("That is an invalid option, try again")

    printLineBreak()

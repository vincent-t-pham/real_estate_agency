# This file will include me hoping and praying that this all works

from user import User
import logInSignIn

print("Welcome to app thing")
success = False
while(not success):
    print("Choose an option [sign in] [log in]")
    firstChoice = input("Selection: ")
    firstChoice = firstChoice.lower()
    firstChoice = firstChoice.replace(" ", "")
    
    if firstChoice == 'signin':
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            if logInSignIn.signIn(user):
                print("Sign In Successful")
                success = True
                break
            else:
                print("Sign In Unsuccessful, Try Again")
    
    elif firstChoice == 'login':
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            if logInSignIn.logIn(user):
                print("Log In Successful")
                success = True
                break
            else:
                print("Log In Unsuccessful, Try Again")

    else:
        print("That is an invalid option, try again")


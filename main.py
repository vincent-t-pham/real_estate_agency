from LogInSystem import logInSignIn as log

# Get username
username = log.logInSignUp()

# Check if user is an admin
if log.isAdmin(username):
    # Admin options
    pass
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
    # Landlord options
    pass

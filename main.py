from LogInSystem import logInSignIn as log

# Get username
username = log.logInSignIn()

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
elif log.isOwner(username):
    # Owner options
    pass

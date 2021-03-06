# SJSU CMPE 138 Spring 2022 TEAM 11

# Admins can create new agents
# Create agent account with password and username in users.db
# Add agent info to agent table in agency.db

# Admins can delete owners
# Delete information from users.db
# Delete information from owner table in agency.db

# Admins can delete clients
# Delete information from users.db
# Delete information from client table in agency.db

import sqlite3 as sql
import sys
sys.path.append('./../real_estate_agency/LogInSystem')
from LogInSystem.user.user import User
from LogInSystem import logInSignIn as log

# Create a new Agent account for users.db and the agent table in agency.db 
def addNewAgent():
    # Create agent account for users.db
    print("Creating a new Agent account")
    
    agentUsername = ''
    
    timeOutCounter = 0
    while timeOutCounter < 4:
        agent = log.collectUserInfo()
        if log.SignUp(agent):
            print("New agent account made")
            agentUsername = agent.username
            break
        else:
            print("Sign up unsuccessful, try again\n")
            if (3 - timeOutCounter) > 1:
                print("%d attempts remaining" % (3 - timeOutCounter))
            elif (3 - timeOutCounter) == 1:
                print("1 attempt remaining")
            timeOutCounter += 1

    # Get agent info
    agentName = input("Agent name: ")
    agentEmail = input("Agent email: ")
    agentPhone = input("Agent phone number (### ### ####): ").replace(" ", "")
    
    # Add agent info to the agent table in agency.db
    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("INSERT INTO Agent VALUES (?, ?, ?, ?)", (agentUsername, agentName, agentEmail, agentPhone))
    conn.commit()
    conn.close()

# Deletes an agent account from users.db and the agent table in agency.db
def deleteAgent():
    print("Which agent would you like to delete?")
    agents = printAllAgents()
    index = int(input("Agent #: "))
    userName = agents[index - 1]

    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("DELETE FROM agent WHERE Agent_id = ?", (userName,))
    conn.commit()
    conn.close()

    # Delete from users database
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("DELETE FROM users WHERE Username = ?", (userName,))
    conn.commit()
    conn.close()

    print("Agent removed")

# Print agent usernames and names
# Also returns a list of the usernames from query result
def printAllAgents():
    conn = sql.connect("agency.db")
    c = conn.cursor()

    c.execute("SELECT Agent_id,Name FROM Agent")
    result = c.fetchall()
    conn.close()

    print(result)

    count = 1
    for agent in result:
        print("Agent [{}]".format(count))
        print("Username: {}".format(agent[0]))
        print("Name: {}".format(agent[1]))
        print("--------------------------")
        count += 1

    usernames = [agent[0] for agent in result]
    return usernames

# Delete a client
def deleteClient():
    print("Which client do you want to delete?")
    clients = printAllClients()
    index = int(input("Client #: "))
    userName = clients[index - 1]

    # Delete from agency database
    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("DELETE FROM Client WHERE Username = ?", (userName,))
    conn.commit()
    conn.close()

    # Delete from users database
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("DELETE FROM users WHERE Username = ?", (userName,))
    conn.commit()
    conn.close()

    print("Client Removed")

# Print client usernames and names
# Also returs a list of the usernames from the query result
def printAllClients():
    conn = sql.connect("agency.db")
    c = conn.cursor()

    c.execute("SELECT Username, Name FROM Client")
    result = c.fetchall()
    conn.close()

    count = 1
    for client in result:
        print("Client [{}]".format(count))
        print("Username: {}".format(client[0]))
        print("Name: {}".format(client[1]))
        print("--------------------------")
        count += 1

    usernames = [client[0] for client in result]
    return usernames

# Delete an owner
def deleteOwner():
    print("Which owner do you want to delete?")
    owners = printAllOwners()
    index = int(input("Owner #: "))
    userName = owners[index - 1]

    conn = sql.connect('agency.db')
    c = conn.cursor()

    c.execute("DELETE FROM Owner WHERE Username = ?", (userName,))
    conn.commit()
    conn.close()

    # Delete from users database
    conn = sql.connect('users.db')
    c = conn.cursor()

    c.execute("DELETE FROM users WHERE Username = ?", (userName,))
    conn.commit()
    conn.close()
    
    print("Owner Removed")

# Print client usernames and names
# Also returs a list of the usernames from the query result
def printAllOwners():
    conn = sql.connect("agency.db")
    c = conn.cursor()

    c.execute("SELECT Username, Name FROM Owner")
    result = c.fetchall()
    conn.close()

    count = 1
    for owner in result:
        print("Owner [{}]".format(count))
        print("Username: {}".format(owner[0]))
        print("Name: {}".format(owner[1]))
        print("--------------------------")
        count += 1

    usernames = [owner[0] for owner in result]
    return usernames

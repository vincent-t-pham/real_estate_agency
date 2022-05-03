# A Seller can select an agent out of a list of available agents
    # Agent [1]: name goes here
import sqlite3
import logging

# Logging File 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('database.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# A Landlord can select an agent out of a list of available agents
    # Agent [1]: name goes here
def selectAgent():
    #Supposed to connect Owner to Landlord to Agent in SQL, needs an entry into Agent
    conn = sqlite3.connect('agency.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * From Agent")  
    except:
        logger.exception("Failed query.")
    else:
        logger.info("SELECT * From Agent")
    result = c.fetchall()
    print("                        ******** AGENTS LIST ********")
    agents = printAgents(result)

# Application then prints out the agent information so client can contact them

def printAgents(result):
    count = 1
    for agent in result:
        print("Agent [{}]".format(count))
        print(agent)
        count+=1

    propertyIDs = [prop[0] for prop in result]
    return propertyIDs

# Application then prints out the agent information so client can contact them

import LogInSystem.logInSignIn as log
import argparse

parser = argparse.ArgumentParser(description='Print users, admins, or delete')
parser.add_argument('--c', type=str)
arg = parser.parse_args()

if arg.c == 'users' or arg.c == 'u':
    log.utilGetAllUsers()
elif arg.c == 'admins' or arg.c == 'a':
    log.utilGetAllAdmins()
elif arg.c == 'delete' or arg.c == 'd':
    log.utilDeleteAll()


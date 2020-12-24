import sys, time
import billy
import auth.user
version = 'v1.0'


username = input("Username: ")
password = input("Password: ")
if auth.user.checkCreds(username, password):
    print("Logged In")
    billy = billy.Billy(version)
    billy.loadModules()
    billy.loadMods()
    billy.main()
else:
    print("Incorrect Username or Password")

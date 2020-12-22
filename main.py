import sys, time
import api.user, api.server
import billy

checkServer = api.server.severStatus()

if checkServer:
    username = input("Username: ")
    password = input("Password: ")
    login = api.user.userAuth(username, password)
    if login:
        print("Logged In")
        billy = billy.Billy()
        #billy.loadModules()
        billy.loadMods()
        billy.main()
    else:
        print("Incorrect Username or Password")

else:
    print("Server Error, check your internet connection")
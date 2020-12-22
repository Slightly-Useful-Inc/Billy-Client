import sys, time
import api.user, api.server
import mods.modHandler

checkServer = api.server.severStatus()

if checkServer:
    username = input("Username: ")
    password = input("Password: ")
    login = api.user.userAuth(username, password)
    if login:
        print("Logged In")
        mods.modHandler.main()
        while True:
            command = input("Billy v1.0>")
            mods.modHandler.runThough(command)
    else:
        print("Incorrect Username or Password")

else:
    print("Server Error, check your internet connection")
import sys, time
import voice.reqRes
import api.user, api.server


checkServer = api.server.severStatus()

if checkServer:
    username = input("Username: ")
    password = input("Password: ")
    login = api.user.userAuth(username, password)
    if login:
        req = voice.reqRes.reqRes()

        time.sleep(1)
        req.billyTalk("How can I help you!")
        while 1:
            req.voice_data = req.get_audio()
            req.respond(req.voice_data)
    else:
        print("Incorrect Username or Password")

else:
    print("Server Error, check your internet connection")
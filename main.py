import requests

def checkServer():
    online = requests.get("http://localhost/")
    if str(online.json()) == "{'status': 200}":
        return True
    else:
        return False

if checkServer():
    print("Servers Are Up")
else:
    print("Servers Do Be Down")
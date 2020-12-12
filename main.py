import requests

def checkServer():
    try:
        online = requests.get("http://localhost/")
        if str(online.json()) == "{'status': 200}":
            return True
        elif str(online.json()) == "{'status': 503":
            return False
    except Exception:
        return False


if checkServer():
    print("Servers Are Up")
else:
    print(checkServer())
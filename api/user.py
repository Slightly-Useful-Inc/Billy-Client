import requests



def userAuth(username, password):
    try:
        request = requests.request("GET", f"http://localhost/auth/{username}/{password}")
        if request.status_code == 200:
            return True
        else:
            return False
    except:
        return False

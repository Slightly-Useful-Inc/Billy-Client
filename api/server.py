import requests


def severStatus():
    
    try:
        request = requests.request("GET", "http://localhost")
        if request.status_code == 200:
            return True
        else:
            return False
    except:
        return False
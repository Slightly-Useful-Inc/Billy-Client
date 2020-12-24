import hashlib
import json
from pathlib import Path
import os

def checkCreds(username, password):
    username_object = hashlib.sha256(username.encode())
    password_object = hashlib.sha256(password.encode())
    username_hash = username_object.hexdigest()
    password_hash = password_object.hexdigest()
    username_object2 = hashlib.sha256(username_hash.encode())
    password_object2 = hashlib.sha256(password_hash.encode())
    
    with open('auth/userInfo.json') as userInfo:
        info = json.load(userInfo)
        if info["username"] == username_object2.hexdigest() and info["password"] == password_object2.hexdigest():
            return True
        else:
            return False

import requests
import json

class api:
    def __init__(self):
        pass

    def quote(self):
        a = requests.get("https://api.quotable.io/random")
        b = a.json()
        quote = b['content']
        author = b['author']
        return {"quote":quote,"author": author, "join": "@ZeroXCoderZChat"}
        
        
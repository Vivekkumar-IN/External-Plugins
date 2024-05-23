import requests
import json

class api:
    def __init__(self):
        pass

    def quote(self):
        qut = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x71\x75\x6f\x74\x61\x62\x6c\x65\x2e\x69\x6f\x2f\x72\x61\x6e\x64\x6f\x6d"
        a = requests.get(qut)
        b = a.json()
        quote = b['content']
        author = b['author']
        return {"quote": quote,"author": author, "join": "@ZeroXCoderZChat"}
        
        
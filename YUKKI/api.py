from random_word import RandomWords
import requests
import json
from googletrans import Translator


translated_text = translator.translate('Hello, world!', dest='es')



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
 
    def randomword(self):
        r = RandomWords()
        result = r.get_random_word()
        return {"word": result,"join": "@ZeroXCoderZChat"}

    def translate(self, query: str, lang)
        translator = Translator()
        results = translator.translate(query, dest=lang)
        return {"query": query, "translation": results,"join": "@ZeroXCoderZChat"}
        
        
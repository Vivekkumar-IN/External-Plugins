# this api belongs to nep coders of @DEVSNP
import requests

class Ai:
    def __init__(self):
        pass

    def chatgpt(self, query):
        response = requests.get(
            f"https://chatgpt.apinepdev.workers.dev/?question={query}"
        )
        if response.status_code == 200:
            result = response.json()["answer"]
            return {"results":result,"join": "@ZeroXCoderZChat", "success": True}

    def imagine(self, query):
        result = f"https://aiimage.hellonepdevs.workers.dev/?prompt={query}"
        return result
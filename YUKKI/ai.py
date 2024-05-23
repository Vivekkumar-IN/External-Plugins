import requests
from MukeshAPI import api as MAPI

class Ai:
    def __init__(self):
        pass

    def chatgpt(self, query):
        response = requests.get(
         f"https://chatgpt.apinepdev.workers.dev/?question={query}"
        )
        # this api belongs to nep coders of @DEVSNP
        if response.status_code == 200:
            result = response.json()["answer"]
            return {"results":result,"join": "@ZeroXCoderZChat", "success": True}

    def imagine(self, query):
        result = f"https://aiimage.hellonepdevs.workers.dev/?prompt={query}"
        return result


# i stored this apis or function from MukeshApi libraray and its develeoper is @Itz_legendCoder
class Mukesh:
    def __init__(self):
        pass

    def gemini(self, query):
        a = MAPI.gemini(query)
        results = a['results']
        return {"results":results,"join": "@ZeroXCoderZChat", "success": True}

        
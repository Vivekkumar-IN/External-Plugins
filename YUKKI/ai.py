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
            return result
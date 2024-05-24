'''MIT License

Copyright (c) present Vivekkumar-IN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
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
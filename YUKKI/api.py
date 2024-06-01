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
SOFTWARE.'''

import os
import json
import requests
from io import BytesIO
from random_word import RandomWords
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file, Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name='RAM SIYA RAM')

class api:
    def __init__(self):
        pass

    def quote(self):
        qut = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x71\x75\x6f\x74\x61\x62\x6c\x65\x2e\x69\x6f\x2f\x72\x61\x6e\x64\x6f\x6d"
        a = requests.get(qut)
        b = a.json()
        quote = b['content']
        author = b['author']
        return {"quote": quote, "author": author, "join": "@ZeroXCoderZChat"}
 
    def randomword(self):
        r = RandomWords()
        result = r.get_random_word()
        return result


    def write(self, text):
        tryimg = "https://graph.org/file/1f8d00177ac2429b101b9.jpg"
        tryresp = requests.get(tryimg)
        img = Image.open(BytesIO(tryresp.content))
        draw = ImageDraw.Draw(img)
        font_url = "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf"
        font_response = requests.get(font_url)
        font = ImageFont.truetype(BytesIO(font_response.content), 24)

        x, y = 150, 140
        lines = []
        if len(text) <= 55:
            lines.append(text)
        else:
            all_lines = text.split("\n")
            for line in all_lines:
                if len(line) <= 55:
                    lines.append(line)
                else:
                    k = len(line) // 55
                    lines.extend(line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2))
    
    
    
        umm = lines[:25]
        
        line_height = font.getbbox("hg")[3]
        linespacing = 41
        for line in umm:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + linespacing
        a = self.randomword()
        file = f"write_{a}.jpg"
        img.save(file)
        if os.path.exists(file):
            upload_path = upload_file(file)
            url = f"https://telegra.ph{upload_path[0]}"
            os.remove(file)
            return url

    def carbon(self, code):
        url = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x63\x61\x72\x62\x6f\x6e\x61\x72\x61\x2e\x73\x6f\x6c\x6f\x70\x6f\x76\x2e\x64\x65\x76\x2f\x61\x70\x69\x2f\x63\x6f\x6f\x6b"

        response = requests.post(url, json={"code": code})
        image = BytesIO(response.content)
    
        a = self.randomword()
        image.name = f"{a}.png"

        with open(image.name, 'wb') as f:
            f.write(image.getbuffer())

        if os.path.exists(image.name):
            upload_path = upload_file(image.name)
            url = f"https://telegra.ph{upload_path[0]}"
            os.remove(image.name)
            return url

    def chatgpt(self, query):
        response = requests.get(
         f"https://chatgpt.apinepdev.workers.dev/?question={query}"
        )
        # this api belongs to nep coders of @DEVSNP
        if response.status_code == 200:
            result = response.json()["answer"]
            return {"results":result,"join": "@ZeroXCoderZChat", "success": True}

    def imagine(self, query):
        image_url = f"https://aiimage.hellonepdevs.workers.dev/?prompt={query}"
        response = requests.get(image_url)
        a = self.randomword()
        image_path = f"temp{a}_image.jpg"
        with open(image_path, "wb") as file:
            file.write(response.content)

        uploaded_file = upload_file(image_path)

        os.remove(image_path)
        return f"https://telegra.ph{uploaded_file[0]}"

    def telegraph(self, title, query):
        '''
        This project includes code from the python273's telegraph library, which is licensed under the MIT License.

        MIT License
        Copyright (c) 2018 python273

        '''
        response = telegraph.create_page(
        title,
        html_content=query
        )
        url = response['url']
        return {"results":url,"join": "@ZeroXCoderZChat", "success": True}


    def advice(self):
        response = requests.get("https://api.safone.dev/advice")
        result = response.json()["advice"]
            return {"results":result,"join": "@ZeroXCoderZChat", "success": True}


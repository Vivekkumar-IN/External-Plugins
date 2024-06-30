import os
import json
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from telegraph import upload_file, Telegraph
from .errors import InvalidAmountError
from .functions import MORSE_CODE_DICT

telegraph = Telegraph()

telegraph.create_account(short_name="RAM SIYA RAM")


class TheApi:
    def __init__(self):
        pass

    def quote(self):
        qut = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x71\x75\x6f\x74\x61\x62\x6c\x65\x2e\x69\x6f\x2f\x72\x61\x6e\x64\x6f\x6d"
        a = requests.get(qut)
        b = a.json()
        quote = b["content"]
        author = b["author"]
        return f"{quote}\n\nauthor - {author}"

    def randomword(self):
        url = f"https://random-word-api.herokuapp.com/word?number=1"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return "None"

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
                    lines.extend(
                        line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2)
                    )

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

        with open(image.name, "wb") as f:
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
            return response.json()["answer"]

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
        response = telegraph.create_page(title, html_content=query)
        return response["url"]

    def get_advice(self):
        try:
            results = requests.get("https://api.adviceslip.com/advice").json()["slip"][
                "advice"
            ]
            return results
        except requests.exceptions.RequestException as e:
            return e

    def get_jokes(self, amount=1):
        if amount > 10 or amount < 1:
            raise InvalidAmountError(amount)
        response = requests.get(
            f"https://v2.jokeapi.dev/joke/Any?type=single&amount={amount}"
        )
        jokes_data = response.json()

        if amount == 1:
            jokes = {"jokes": {"joke": jokes_data["joke"]}}
        else:
            jokes = {
                "jokes": {
                    f"joke{i+1}": joke["joke"]
                    for i, joke in enumerate(jokes_data["jokes"])
                }
            }

        return json.dumps(jokes)

    def get_hindi_jokes(self):
        JOKE_API_ENDPOINT = "https://hindi-jokes-api.onrender.com/jokes?api_key=93eeccc9d663115eba73839b3cd9"
        response = requests.get(JOKE_API_ENDPOINT).json()
        if response["status"]:
            results = response["jokeContent"]
            return results

    def get_uselessfact(self):
        results = requests.get(
            "https://uselessfacts.jsph.pl/api/v2/facts/random"
        ).json()["text"]
        return results

    def gen_hashtag(self, text):
        url = "https://all-hashtag.com/library/contents/ajax_generator.php"

        data = {
            "keyword": text,
            "filter": "top",
        }
        response = requests.post(url, data=data)
        soup = BeautifulSoup(response.text, "html.parser")
        hashtags_div = soup.find("div", id="copy-hashtags")
        hashtags = hashtags_div.text.strip() if hashtags_div else ""
        similar_hashtags_div = soup.find("div", id="copy-hashtags-similar")
        similar_hashtags = (
            similar_hashtags_div.text.strip() if similar_hashtags_div else ""
        )
        return f"Hashtags:\n{hashtags}\n\n Similar hashtags:\n{similar_hashtags}"

    def morse_code(self, txt):
        MORSE_CODE_DICT_REVERSED = {
            value: key for key, value in MORSE_CODE_DICT.items()
        }
        is_morse = all(char in ".- /" for char in txt)

        if is_morse:
            decoded_message = ""
            words = txt.split(" / ")
            for word in words:
                for morse_char in word.split():
                    if morse_char in MORSE_CODE_DICT_REVERSED:
                        decoded_message += MORSE_CODE_DICT_REVERSED[morse_char]
                    else:
                        return f"Error: Morse code '{morse_char}' not recognized."
                decoded_message += " "
            return decoded_message.strip()
        else:
            encoded_message = ""
            for char in txt.upper():
                if char in MORSE_CODE_DICT:
                    encoded_message += MORSE_CODE_DICT[char] + " "
                else:
                    return f"Error: Character '{char}' cannot be encoded in Morse code."
            return encoded_message.strip()

    def wikipedia(self, query):
        search_url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }

        response = requests.get(search_url, params=params)

        if response.status_code == 200:
            data = response.json()
            search_results = data.get("query", {}).get("search", [])

            if search_results:
                top_result = search_results[0]
                page_id = top_result["pageid"]
                summary_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts|pageimages&exintro&explaintext&piprop=thumbnail&pithumbsize=500&format=json&pageids={page_id}"
                summary_response = requests.get(summary_url)

                if summary_response.status_code == 200:
                    summary_data = summary_response.json()
                    pages = summary_data.get("query", {}).get("pages", {})
                    page_info = pages.get(str(page_id), {})
                    image_url = page_info.get("thumbnail", {}).get(
                        "source", "No image available"
                    )

                    return {
                        "title": top_result["title"],
                        "summary": page_info.get("extract", "No summary available."),
                        "url": f"https://en.wikipedia.org/?curid={page_id}",
                        "image_url": image_url,
                    }
                else:
                    return {"error": "Failed to fetch the page summary"}
            else:
                return {"error": "No search results found"}
        else:
            return {"error": "Failed to fetch search results"}

    def github_search(self, query, max_results=10):
        url = "https://api.github.com/search/repositories"
        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            results = response.json()
            repositories = results["items"]
            repo_list = []
            for repo in repositories:
                repo_info = {
                    "name": repo["name"],
                    "full_name": repo["full_name"],
                    "description": repo["description"],
                    "url": repo["html_url"],
                }
                repo_list.append(repo_info)
            return repo_list
        else:
            return {"error": f"Error: {response.status_code} - {response.json()}"}

    def words(self, num_words: int):
        url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    def cat(self):

        r = requests.get("https://api.thecatapi.com/v1/images/search")
        if r.status_code == 200:
            return r.json()[0]["url"]

    def dog(self):
        r = requests.get("https://random.dog/woof.json")
        if r.status_code == 200:
            return r.json()["url"]


api = TheApi()

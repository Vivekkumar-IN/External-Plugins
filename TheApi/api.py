import os
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
        """
        Fetches a random quote from an API and returns it along with the author.

        Returns:
        str: A formatted string containing the quote and its author.

        EXAMPLE:

        ```python
        from TheApi import api
        
        quote = api.quote()
       
        print(quote)

   
        Results
        
        Beware lest you lose the substance by grasping at the shadow.
        author - Aesop
        """
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

    def get_jokes(self, amount):
        if not isinstance(amount, int):
            raise ValueError("The amount must be an integer.")

        if amount > 10 or amount < 1:
            raise InvalidAmountError(amount)

        response = requests.get(
            f"https://v2.jokeapi.dev/joke/Any?type=single&amount={amount}"
        )
        jokes_data = response.json()

        if amount == 1:
            return jokes_data["joke"]
        else:
            jokes = [joke["joke"] for joke in jokes_data["jokes"]]
            formatted_jokes = "\n\n".join(
                f"{i+1}. {joke}" for i, joke in enumerate(jokes)
            )
            return formatted_jokes

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

    def github_search(self, query, search_type="repositories", max_results=10):
        valid_search_types = [
            "repositories",
            "users",
            "organizations",
            "issues",
            "pull_requests",
            "commits",
            "labels",
            "topics",
        ]
        if search_type not in valid_search_types:
            return {
                "error": f"Invalid search type. Valid types are: {valid_search_types}"
            }

        if search_type == "pull_requests":
            url = "https://api.github.com/search/issues"
            query += " type:pr"
        elif search_type == "organizations":
            url = "https://api.github.com/search/users"
            query += " type:org"
        elif search_type == "labels":
            url = "https://api.github.com/search/labels"
        elif search_type == "topics":
            url = "https://api.github.com/search/topics"
        else:
            url = f"https://api.github.com/search/{search_type}"

        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}

        try:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                results = response.json()
                items = results["items"]
                result_list = []

                for item in items:
                    if search_type == "repositories":
                        item_info = {
                            "name": item["name"],
                            "full_name": item["full_name"],
                            "description": item["description"],
                            "url": item["html_url"],
                            "language": item.get("language"),
                            "stargazers_count": item.get("stargazers_count"),
                            "forks_count": item.get("forks_count"),
                        }
                    elif search_type == "users" or search_type == "organizations":
                        item_info = {
                            "login": item["login"],
                            "id": item["id"],
                            "url": item["html_url"],
                            "avatar_url": item.get("avatar_url"),
                            "type": item.get("type"),
                            "site_admin": item.get("site_admin"),
                            "name": item.get("name"),
                            "company": item.get("company"),
                            "blog": item.get("blog"),
                            "location": item.get("location"),
                            "email": item.get("email"),
                            "bio": item.get("bio"),
                            "public_repos": item.get("public_repos"),
                            "public_gists": item.get("public_gists"),
                            "followers": item.get("followers"),
                            "following": item.get("following"),
                        }
                    elif search_type == "issues" or search_type == "pull_requests":
                        item_info = {
                            "title": item["title"],
                            "user": item["user"]["login"],
                            "state": item["state"],
                            "url": item["html_url"],
                            "comments": item.get("comments"),
                            "created_at": item.get("created_at"),
                            "updated_at": item.get("updated_at"),
                            "closed_at": item.get("closed_at"),
                        }
                    elif search_type == "commits":
                        item_info = {
                            "sha": item["sha"],
                            "commit_message": item["commit"]["message"],
                            "author": item["commit"]["author"]["name"],
                            "date": item["commit"]["author"]["date"],
                            "url": item["html_url"],
                        }
                    elif search_type == "labels":
                        item_info = {
                            "name": item["name"],
                            "color": item["color"],
                            "description": item.get("description"),
                            "url": item["url"],
                        }
                    elif search_type == "topics":
                        item_info = {
                            "name": item["name"],
                            "display_name": item.get("display_name"),
                            "short_description": item.get("short_description"),
                            "description": item.get("description"),
                            "created_by": item.get("created_by"),
                            "url": item["url"],
                        }

                    result_list.append(item_info)
                return result_list
            else:
                return {"error": f"Error: {response.status_code} - {response.json()}"}

        except requests.exceptions.RequestException as e:
            return {"error": f"Request exception: {e}"}

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

    def help(self, method_name):
        """
        Retrieves the help documentation for a given method.

        Args:
        method_name (str): The name of the method to retrieve help for.

        Returns:
        str: The help documentation for the specified method.
        """
        method = getattr(self, method_name, None)
        if method and callable(method):
            docstring = method.__doc__
            return docstring.strip() if docstring else f"No help available for method '{method_name}'."
        else:
            return f"Method '{method_name}' not found."


api = TheApi()

from google_play_scraper import search, permissions

class App:
    def __init__(self):
        pass

    def search(self, query, lang='en', country='us', n_hits=3):
        result = search(
            query,
            lang=lang,
            country=country,
            n_hits=n_hits
        )
        return result
    
    def permissions(self, query, lang='en', country='us'):
        result = permissions(
            query,
            lang=lang,
            country=country,
        )
        return result
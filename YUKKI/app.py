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


from google_play_scraper import search, permissions

class APP:

    '''
    This project includes code from the google_play_scraper library, which is licensed under the MIT License.

    MIT License
    Copyright (c) 2019 PlanB

    '''

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


App =APP()
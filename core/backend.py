import requests
import urllib.request as request
from bs4 import BeautifulSoup
from thefuzz import fuzz

API_KEY = 'AIzaSyDDqbiRfcQdH4-O7BRHgNEDER6SwFSIGG8'
SEARCH_ENGINE_ID = '65bcfb25f936c47bb'


def plagiarism_checker(document):
    result = []
    url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={document}'

    response = requests.get(url)
    data = response.json()

    for item in data.get('items', []):
        link = item.get('link')

        request_site = request.Request(link, headers={"User-Agent": "Mozilla/5.0"})
        web_url = request.urlopen(request_site)
        data = web_url.read()

        soup = BeautifulSoup(data, 'html.parser')
        plain_text = soup.get_text()

        lines = (line.strip() for line in plain_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        fuzzy_ratio = fuzz.ratio(document, text)
        fuzzy_partial_ratio = fuzz.partial_ratio(document, text)

        result.append({
            'fuzzy_partial_ratio': fuzzy_partial_ratio,
            'fuzzy_ratio': fuzzy_ratio,
            'link': link
        })
        break

    return result

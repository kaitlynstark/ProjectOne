import requests
import sys

def fetch_wikipedia_data(article_title):
    URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": article_title,
        "rvprop": "timestamp|user",
        "rvlimit": 30,
        "redirects": 1
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Error: Cannot connect to Wikipedia.")
        sys.exit(3)

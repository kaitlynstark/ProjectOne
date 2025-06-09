import requests
import sys

#Get title of a Wikipedia article
def get_article_title_from_command_line():
    if len(sys.argv) < 2:
        print("Error: You have to provide the name of a Wikipedia article.")
        sys.exit(1)
    return ' '.join(sys.argv[1:])  # Allows titles like "Taylor Swift"

#Fetch data from Wikipedia API
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

#Process Wikipedia API response
def process_wikipedia_response(data):
    try:
        if 'redirects' in data.get('query', {}):
            for redirect in data['query']['redirects']:
                print(f"Redirected to {redirect['to']}")

        pages = data['query']['pages']
        for page_id in pages:
            page = pages[page_id]
            if 'revisions' not in page:
                print("No revisions found for this article.")
                sys.exit(2)

            revisions = page['revisions']
            for rev in revisions:
                print(f"{rev['timestamp']} {rev['user']}")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(2)

#Main program function
def main():
    article_title = get_article_title_from_command_line()
    data = fetch_wikipedia_data(article_title)
    process_wikipedia_response(data)

if __name__ == "__main__":
    main()
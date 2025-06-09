import sys

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

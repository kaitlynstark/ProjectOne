from article_utils import get_article_title_from_command_line
from api_utils import fetch_wikipedia_data
from output_utils import process_wikipedia_response

def main():
    article_titles = get_article_title_from_command_line()
    data = fetch_wikipedia_data(article_titles)
    process_wikipedia_response(data)

if __name__ == "__main__":
    main()

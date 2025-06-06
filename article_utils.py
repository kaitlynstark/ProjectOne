import sys

def get_article_title_from_command_line():
    if len(sys.argv) != 2:
        print("Error: You have to provide the name of a Wikipedia article.")
        sys.exit(1)
    return sys.argv[1]

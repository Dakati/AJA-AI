import webbrowser
import urllib.parse


def google(query):
    query = query.strip()

    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)

    webbrowser.open(url)
    print("GOOGLE URL:", url)

    return f"Searching Google for {query}"


def youtube(query):
    query = query.strip()

    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)

    webbrowser.open(url)

    return f"Searching YouTube for {query}"
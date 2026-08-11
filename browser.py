import webbrowser
import urllib.parse


def google_search(query):
    query = query.strip()

    if not query:
        return "What should I search for?"

    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    webbrowser.open_new_tab(url)

    return f"Searching Google for {query}"


def youtube_search(query):
    query = query.strip()

    if not query:
        return "What should I search on YouTube?"

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote_plus(query)
    )

    webbrowser.open_new_tab(url)

    return f"Searching YouTube for {query}"


def open_google():
    webbrowser.open_new_tab("https://www.google.com")
    return "Opening Google..."


def open_youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    return "Opening YouTube..."


def open_website(website):

    website = website.strip()

    if not website:
        return "Please provide a website."

    if not website.startswith(("http://", "https://")):
        website = "https://" + website

    webbrowser.open_new_tab(website)

    return f"Opening {website}..."
def browser_back():
    webbrowser.open_new_tab("javascript:history.back()")
    return "Going back..."


def browser_forward():
    webbrowser.open_new_tab("javascript:history.forward()")
    return "Going forward..."


def open_new_tab():
    webbrowser.open_new_tab("about:blank")
    return "Opening a new tab..."


def refresh_page():
    webbrowser.open_new_tab("about:blank")
    return "Browser refresh command received..."
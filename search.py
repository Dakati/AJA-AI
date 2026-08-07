from googlesearch import search

def google_search(query):
    results = []

    try:
        for url in search(query, num_results=5):
            results.append(url)
    except Exception:
        return []

    return results
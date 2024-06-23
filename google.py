# Acessa uma página do google e printar os resultados

import requests
from bs4 import BeautifulSoup


def google_search(query):
    url = "https://duckduckgo.com/html/"
    params = {"q": query, "num": 5}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for result in soup.find_all("div", class_="result")[:5]:
        title_element = result.find("a", class_="result__a")
        if title_element:
            title = title_element.text
            link = title_element["href"]
        else:
            title = "No title"
            link = "No link"

        snippet_element = result.find("a", class_="result__snippet")
        if snippet_element:
            snippet = snippet_element.text
        else:
            snippet = "No snippet"

        results.append({"title": title, "link": link, "snippet": snippet})

    return results if results else []


query = "Undertale"
results = google_search(query)
for result in results:
    print(result)

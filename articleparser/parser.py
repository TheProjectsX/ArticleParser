from googlesearch import search
import requests
from bs4 import BeautifulSoup
import newspaper
import wikipedia
from html2text import HTML2Text

# Create HTML2Text Object
html2text = HTML2Text()


# Get Actual text Contents of Wikipedia
def parseWikipediaContent(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content_div = soup.find('div', id='mw-content-text')
    content = ""
    for element in content_div.find_all(['p', 'h2', 'h3']):
        content += element.text.strip() + "\n"

    if (content == ""):
        query = url.split("/")[-1]
        content = wikipedia.summary(
            query, sentences=10, auto_suggest=False, redirect=False)

    return content


# Get the text article from a Url
def parseArticle(url: str, timeout=10, max_length=14400, markup=False, ignore_links=False, customMarkupRules={}):
    """
    Description: Parse article from a URL
    Parameters:
        url: Article Url
        timeout: Timeout of the Parsing time of URL's article (Default: 10)
        man_length: Maximum Length of Text you Need
        markup: To parse the content while Converting HTML to Markup (Default: False)
        ignore_links: Only useful when `markup = True`. Will ignore the Links from Contents if True, else will convert them to Markup Format (Default: False)
        customMarkupRules: There are many Markup Rules can be set in the HTML2Text Object. We can't add every one of them as Parameters. So, pass them as a Dictionary (Default: {})
    """
    if (markup):
        customMarkupRules["ignore_links"] = ignore_links
        for key, value in customMarkupRules.items():
            setattr(html2text, key, value)

    domain = url.replace(
        "https://", "", 1).replace("http://", "", 1).split("/")[0]
    if ("wikipedia.org" in domain):
        title = url.split("/")[-1].replace("_", " ")
        content = parseWikipediaContent(url)

    else:
        try:
            html = requests.get(url, timeout=timeout).text
            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.getText()

            if (markup):
                content = html2text.handle(html)
            else:
                content = newspaper.fulltext(html)
        except Exception as e:
            return None

    articleData = {
        "title": title,
        "content": content[:max_length]
    }
    return articleData


# Get google search results
def getGoogleSearchResults(query, num_results=3):
    results = list(search(query, advanced=True, num_results=num_results))

    searchResults = []
    for result in results:
        searchResults.append({
            "url": result.url,
            "title": result.title,
            "description": result.description
        })

    return searchResults


# Main Function the get the Articles
def getArticles(query: str, num_results=5, timeout=10, max_length=14400, markup=False, ignore_links=False, customMarkupRules={}):
    """
    Description: Get Desired Articles's Contents right from Google Search!
    Parameters:
        query: Your Search Query
        num_results: Number of Results you want to Get (Default: 5). Sometimes article numbers can be wrong.
        timeout: Timeout of the Parsing time of URL's article (Default: 10)
        man_length: Maximum Length of Text you Need
        markup: To parse the content while Converting HTML to Markup (Default: False)
        ignore_links: Only useful when `markup = True`. Will ignore the Links from Contents if True, else will convert them to Markup Format (Default: False)
        customMarkupRules: There are many Markup Rules can be set in the HTML2Text Object. We can't add every one of them as Parameters. So, pass them as a Dictionary (Default: {})

    Return:
        Returns a Generator Object
    """
    searchResults = getGoogleSearchResults(query, num_results=num_results)

    for result in searchResults:
        data = result.copy()
        articleData = parseArticle(
            data["url"], max_length=max_length, timeout=timeout, markup=markup, ignore_links=ignore_links, customMarkupRules=customMarkupRules)
        if (not articleData):
            continue

        data["body"] = articleData["content"]
        yield data


# Test out the Module!
def main():
    query = input("Enter Search Query:> ")
    articlesData = getArticles(query)

    print("\n---- Parsed Data ----\n\n")
    for article in articlesData:
        print("URL:", article["url"])
        print("Title:", article["title"])
        print("Body:", article["body"][:400], "...\n\n")


if (__name__ == "__main__"):
    main()

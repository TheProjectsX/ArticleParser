# Article Parser

Get Articles Data just by Search Query

### Workflow:

- Uses googlesearch_python package to search for Google Search URLs
- Uses requests to get the URL's Webpage data
- Uses bs4, wikipedia and newspaper Libraries to Parse the actual Contents of the URL's
- Uses html2text to convert the HTML content to Markup. Which is decided by user
- Returns a Generator Object containing Search Results

### Installations:

Install using pip

```bash script
pip install git+https://github.com/TheProjectsX/ArticleParser.git
```

## Usages

### Get Articles via Search Query

```python
import articleparser

articlesData = articleparser.getArticles(query="What is Node JS?")
for article in articlesData:
    print("URL:", article["url"])
    print("Title:", article["title"])
    print("Body:", article["body"][:400])
```

### Get Google Search Results

```python
import articleparser

searchResults = articleparser.getGoogleSearchResults(query="What is Node JS?")
for article in articlesData:
    print("URL:", article["url"])
    print("Title:", article["title"])
    print("Description:", article["description"])
```

### Parse Article from a Certain URL

User can pass a certain Webpage URL to parse it's content

```python
import articleparser

article = articleparser.parseArticle(url="")

print("Title:", article["title"])
print("Content:", article["content"][:400])
```

## NOTE:

There are many useful Parameters in each Function.
You can get it's description Just by hovering in them or opening the file!

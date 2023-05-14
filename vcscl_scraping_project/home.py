import requests
from bs4 import BeautifulSoup

url = "https://www.reuters.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("div", {"class": "story-package"})
for article in articles:
    headline = article.find("h3", {"class": "story-title"}).text.strip()
    date = article.find("span", {"class": "timestamp"}).text.strip()
    link = article.find("a", href=True)["href"]
    summary = article.find("p", {"class": "story-summary"}).text.strip()

    print(headline)
    print(date)
    print(link)
    print(summary)











import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
headlines = soup.find_all("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")

for headline in headlines:
    print(headline.text.strip())

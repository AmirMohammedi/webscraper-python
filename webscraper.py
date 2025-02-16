import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')

    return [headline.get_text(strip=True) for headline in headlines]


def scrape_prices(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all(class_='price') 

    return [price.get_text(strip=True) for price in prices]


news_url = "https://www.bbc.com/news"
product_url = "https://books.toscrape.com"

news_headlines = scrape_headlines(news_url)
product_prices = scrape_prices(product_url)

print("News Headlines:", news_headlines)
print("Product Prices:", product_prices)

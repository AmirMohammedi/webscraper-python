# Web Scraper using BeautifulSoup

This Python script scrapes news headlines or product prices from a website using the `requests` library and `BeautifulSoup`.

## Requirements

Before running the script, install the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

Modify the `news_url` or `product_url` variables in the script to specify the target website.

### Scraping News Headlines
To scrape news headlines from a website:
```python
news_url = "https://www.bbc.com/news"
news_headlines = scrape_headlines(news_url)
print("News Headlines:", news_headlines)
```

### Scraping Product Prices
To scrape product prices from an e-commerce site:
```python
product_url = "https://books.toscrape.com/"
product_prices = scrape_prices(product_url)
print("Product Prices:", product_prices)
```

## Notes
- Ensure that the website structure is correctly analyzed before extracting data.
- Websites with JavaScript-rendered content may require Selenium instead of BeautifulSoup.
- Respect the website's `robots.txt` and terms of service before scraping.

## License
This project is open-source and available under the MIT License.


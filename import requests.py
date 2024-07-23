import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    for item in soup.select('.product-item'):
        name = item.select_one('.product-title').get_text(strip=True)
        price = item.select_one('.product-price').get_text(strip=True)
        rating = item.select_one('.product-rating').get_text(strip=True)
        products.append((name, price, rating))
    return products

def save_to_csv(products, filename='products.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(products)

def main(url):
    html = fetch_html(url)
    if html:
        products = parse_html(html)
        if products:
            save_to_csv(products)
            print(f"Saved {len(products)} products to 'products.csv'")
        else:
            print("No products found.")
    else:
        print("Failed to fetch the webpage.")

if __name__ == "__main__":
    # Replace with the URL of the e-commerce website's product listing page you want to scrape
    url = 'https://www.example.com/products'
    main(url)

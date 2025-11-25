# Amazon-Multi-Category-Scraper  

A Python-based web scraper that collects product data from multiple Amazon categories using Selenium.  
This project demonstrates web scraping skills, handling dynamic content, and data extraction for e-commerce analysis.  

## Features  

- Scrapes multiple categories (e.g., Laptops, Headphones)
- Extracts product details:
  - Title
  - Price
  - Rating
  - Reviews
  - Product URL
- Handles multiple pages per category 
- Saves scraped data to a Python list (can easily be exported to CSV/Excel)
- Uses random delays and user-agent rotation to reduce bot detection

## Technologies Used  
- Python 3
- Selenium WebDriver
- ChromeDriver
- fake_useragent` for user-agent rotation
- pandas` for data handling

## How to Run
1. Install dependencies:
```
pip install selenium pandas webdriver-manager fake-useragent
```

2. Run the scraper:
```
python scraper.py
```
3. Scraped data is stored in the all_products list and can be saved to CSV:
```
import pandas as pd
df = pd.DataFrame(all_products)
df.to_csv("amazon_products.csv", index=False)
```
**Notes**
Ensure ChromeDriver version matches your Chrome browser  
Use responsibly and avoid overloading Amazon servers  
Headless mode can be enabled for background execution  

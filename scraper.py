import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

# -----------------------
# Configuration
# -----------------------
categories = {
    "Laptops": "https://www.amazon.com/s?k=laptops",
    "Headphones": "https://www.amazon.com/s?k=headphones"
}

max_pages = 3  # pages per category to scrape

# -----------------------
# Setup Selenium
# -----------------------
ua = UserAgent()
options = Options()
options.headless = True  # Run browser in background
options.add_argument(f"user-agent={ua.random}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

all_products = []

# -----------------------
# Scraping Loop
# -----------------------
for category, url in categories.items():
    for page in range(1, max_pages + 1):
        driver.get(f"{url}&page={page}")
        time.sleep(random.uniform(2, 5))  # random delay

        products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        for p in products:
            try:
                title = p.find_element(By.XPATH, ".//h2/a/span").text
            except:
                title = None
            try:
                price_whole = p.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
                price_fraction = p.find_element(By.XPATH, ".//span[@class='a-price-fraction']").text
                price = price_whole + price_fraction
            except:
                price = None
            try:
                rating = p.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
            except:
                rating = None
            try:
                reviews = p.find_element(By.XPATH, ".//span[@class='a-size-base']").text
            except:
                reviews = None
            try:
                product_url = p.find_element(By.XPATH, ".//h2/a").get_attribute("href")
            except:
                product_url = None

            all_products.append({
                "Category": category,
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Reviews": reviews,
                "URL": product_url
            })

driver.quit()

# -----------------------
# Save to CSV
# -----------------------
df = pd.DataFrame(all_products)
df.to_csv("amazon_products.csv", index=False)
print("Scraping completed! Data saved to amazon_products.csv")

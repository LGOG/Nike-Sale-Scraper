from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# URLs for each category
urls = {
    'Man': "https://www.nike.com/w/mens-sale-shoes-3yaepznik1zy7ok?sort=newest",
    'Woman': "https://www.nike.com/w/womens-sale-shoes-3yaepz5e1x6zy7ok?sort=newest",
    'Unisex': "https://www.nike.com/w/unisex-sale-shoes-3rauvz3yaepzy7ok?sort=newest",
    'All': "https://www.nike.com/w/sale-shoes-3yaepzy7ok?sort=newest"
}

# Selenium setup with headless option and no images
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument('--disable-gpu')  # Disable GPU (sometimes needed for headless mode)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# Disable images
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

driver = webdriver.Chrome(options=options)

# Ask user to choose a category
print("Choose a category: Man, Woman, Unisex, All")
choice = input("Your choice: ").capitalize()

# Get the appropriate URL based on the user's choice
URL = urls.get(choice, "https://www.nike.com/w/sale-shoes-3yaepzy7ok")  # Default to 'All' if invalid choice

print("\033[94mPlease wait, gathering information. This may take a few seconds...\033[0m")  # Blue text
print("\033[92mGreen\033[0m: 50%+ discount")
print("\033[93mOrange\033[0m: 25%-50% discount")
print("\033[91mRed\033[0m: 0%-25% discount")

driver.get(URL)

# Scroll the page to load all items
for _ in range(10):  # Adjust the range as needed for the number of scrolls
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  # Adjust sleep time as needed

# Get the HTML of the page after scrolling
soup = BeautifulSoup(driver.page_source, 'html.parser')
title = soup.select_one('title').get_text() if soup.select_one('title') else 'Nike Sale'

print(f"\n{title}\n")

items = soup.select('.product-card')

# List to hold table data
table_data = []

for item in items:
    name_tag = item.select_one('.product-card__title')
    name = name_tag.get_text(strip=True) if name_tag else 'No name'

    price_spans = item.select('.product-price')
    old_price = "Unknown"
    new_price = "Unknown"
    savings = "N/A"

    if price_spans:
        prices = [price.get_text(strip=True) for price in price_spans if price.get_text(strip=True)]
        if len(prices) == 2:
            old_price, new_price = prices
            try:
                old_price_num = float(old_price.strip('$').replace(',', ''))
                new_price_num = float(new_price.strip('$').replace(',', ''))
                savings_percent = (old_price_num - new_price_num) / old_price_num * -100 / 2
                savings = f"{savings_percent:.2f}%"
            except ValueError:
                savings = "N/A"

    table_data.append([name, old_price, new_price, savings])

# Function to sort the table data by savings percentage
def savings_key(row):
    try:
        return float(row[3].rstrip('%'))
    except ValueError:
        return float('-inf')  # Return a low value for items without savings to move them to the end

# Sort the data by savings percentage
table_data.sort(key=savings_key, reverse=True)

# Function to determine color based on savings percentage
def get_color(savings):
    try:
        savings_value = float(savings.rstrip('%'))
        if savings_value >= 50:
            return "\033[92m"  # Green
        elif 25 <= savings_value < 50:
            return "\033[93m"  # Orange
        else:
            return "\033[91m"  # Red
    except ValueError:
        return "\033[0m"  # Default color

# Print the table with color-coded savings
print("{:30} {:10} {:10} {:8}".format("Name", "Old Price", "New Price", "Savings"))
for row in table_data:
    name, old_price, new_price, savings = row
    color = get_color(savings)
    print(f"{name:30} {old_price:10} {new_price:10} {color}{savings}\033[0m")

# Don't forget to close the browser
driver.quit()

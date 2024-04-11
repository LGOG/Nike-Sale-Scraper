# Nike Sale Scraper

This script automates the process of scraping sale items from Nike's official website, specifically focusing on the shoe category. It fetches data such as the product name, original price, sale price, and the discount percentage. The results are presented in a color-coded format to highlight the level of discount for each product.

## Features

- Automatically scrapes sale data from Nike's website.
- Sorts products by discount percentage.
- Color codes the output based on the discount percentage (Green for high discounts, Orange for moderate discounts, and Red for low discounts).
- Utilizes headless browsing to avoid unnecessary UI load and speed up the process.

## Prerequisites

Before you run the script, ensure you have the following installed:

- Python 3.x
- Selenium
- BeautifulSoup4
- Chrome WebDriver

## Installation

1. **Python 3.x**: Make sure you have Python installed on your machine. You can download it from [the official Python website](https://www.python.org/downloads/).

2. **Required Python packages**: Install the necessary Python packages using pip. Open your terminal or command prompt and run the following commands:

    ```bash
    pip install selenium
    pip install beautifulsoup4
    pip install lxml
    ```

3. **Chrome WebDriver**: Download the Chrome WebDriver from [the ChromeDriver website](https://sites.google.com/chromium.org/driver/). Make sure the version of the WebDriver matches your Chrome browser's version. Extract the downloaded file and place it in a known directory. If you're using a different browser, ensure you download the corresponding WebDriver.

## Usage

1. Clone or download the script from GitHub to your local machine.

2. Open the terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using Python:

    ```bash
    python nike_sale_scraper.py
    ```

4. Follow the on-screen prompts to select the category you wish to scrape.

5. The script will then fetch the sale data from Nike's website and display it in the terminal, color-coded by discount percentage.

## Color Index

- **Green**: Discounts of 50% and above.
- **Orange**: Discounts ranging from 25% to 50%.
- **Red**: Discounts below 25%.

The script simplifies the process of finding the best deals on Nike's website, especially during sale seasons. By automating the data collection and sorting process, it saves time and ensures you get the information you need quickly and efficiently.

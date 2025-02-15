# ==== building the bot ====

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = 'https://www.audible.com/search'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
products = container.find_elements(
    By.XPATH, './/li[contains(@class, "productListItem")]')


book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element(
        By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(
        By.XPATH, './/li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(
        By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length,
})
df_books.to_csv('books.csv', index=False)

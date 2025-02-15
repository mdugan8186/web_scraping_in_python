# ==== headless mode ===

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
# import this for headless mode
from selenium.webdriver.chrome.options import Options


# this will initiate headless mode
options = Options()
# this is the new way to activate headless mode
options.add_argument('--headless=new')
# use this instead of driver.maximize_window
options.add_argument('window-size=1920x1080')


website = 'https://www.audible.com/search'
service = Service(ChromeDriverManager().install())
# add options as the second argument
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
# driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
products = container.find_elements(
    By.XPATH, './/li[contains(@class, "productListItem")]')


book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element(
        By.XPATH, './/h3[contains(@class, "bc-heading")]').text)

    print(product.find_element(
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
df_books.to_csv('books_headless.csv', index=False)

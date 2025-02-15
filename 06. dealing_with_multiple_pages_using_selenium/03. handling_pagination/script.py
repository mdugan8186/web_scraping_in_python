# ==== handling pagination ====

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
# import time for implicit waits
import time


options = Options()
# options.add_argument('--headless=new')
# options.add_argument('window-size=1920x1080')


website = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=adc4b13b-d074-4e1c-ac46-9f54aa53072b&pf_rd_r=6Z3BNK326ZH91DJ8XS8G'
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
driver.maximize_window()


# pagination
pagination = driver.find_element(
    By.XPATH, '//ul[contains(@class, "pagingElements")]')
# if using Xpath it would be this
# //ul[contains(@class, "pagingElements")]/li
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1

book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    # set up an implicit wait so it has time to render the page correctly
    time.sleep(2)
    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    products = container.find_elements(
        By.XPATH, './/li[contains(@class, "productListItem")]')

    for product in products:
        book_title.append(product.find_element(
            By.XPATH, './/h3[contains(@class, "bc-heading")]').text)

        # print(product.find_element(
        #     By.XPATH, './/h3[contains(@class, "bc-heading")]').text)

        book_author.append(product.find_element(
            By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(
            By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    current_page += 1

    try:
        next_page = driver.find_element(
            By. XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df_books = pd.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length,
})
df_books.to_csv('books_pagination.csv', index=False)
